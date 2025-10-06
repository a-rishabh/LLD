from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from .models import ParkingSpot, Vehicle
from .enums import SpotType, VehicleType
from .errors import NoCompatibleSpotError


@dataclass
class ParkingFloor:
    """Represents a single floor in the parking lot."""
    floor_id: int
    spots: List[ParkingSpot] = field(default_factory=list)

    # internal index: SpotType -> [free spot_ids]
    _free_index: Dict[SpotType, List[str]] = field(default_factory=dict, init=False, repr=False)

    def __post_init__(self) -> None:
        """Initialize free index for fast allocation."""
        for spot in self.spots:
            if spot.stype not in self._free_index:
                self._free_index[spot.stype] = []
            if not spot.occupied:
                self._free_index[spot.stype].append(spot.spot_id)
        # deterministic order: lower IDs first
        for s in self._free_index.values():
            s.sort()

    # ---------------- Core Operations ---------------- #

    def find_free_spot(self, vtype: VehicleType) -> Optional[ParkingSpot]:
        """Return the first compatible free spot for this vehicle type."""
        for stype, free_list in self._free_index.items():
            if self._compatible(vtype, stype) and free_list:
                sid = free_list[0]
                return self._get_spot(sid)
        return None

    def assign_vehicle(self, vehicle: Vehicle) -> ParkingSpot:
        """Assign the first available compatible spot to a vehicle."""
        spot = self.find_free_spot(vehicle.vtype)
        if not spot:
            raise NoCompatibleSpotError(f"No compatible free spot on floor {self.floor_id}")
        spot.assign(vehicle)
        # remove from free index
        self._free_index[spot.stype].remove(spot.spot_id)
        return spot

    def free_spot(self, spot_id: str) -> None:
        """Free a spot and update index."""
        spot = self._get_spot(spot_id)
        v = spot.free()
        self._free_index[spot.stype].append(spot_id)
        self._free_index[spot.stype].sort()
        return v

    # ---------------- Helpers ---------------- #

    def available_count(self, stype: SpotType) -> int:
        """Number of free spots of a given type."""
        return len(self._free_index.get(stype, []))

    def _get_spot(self, sid: str) -> ParkingSpot:
        for s in self.spots:
            if s.spot_id == sid:
                return s
        raise ValueError(f"Spot {sid} not found on floor {self.floor_id}")

    @staticmethod
    def _compatible(vtype: VehicleType, stype: SpotType) -> bool:
        """Compatibility logic (mirrors ParkingSpot.can_fit)."""
        if vtype == VehicleType.BIKE:
            return stype in {SpotType.MOTORBIKE, SpotType.COMPACT, SpotType.LARGE}
        if vtype == VehicleType.CAR:
            return stype in {SpotType.COMPACT, SpotType.LARGE}
        if vtype == VehicleType.TRUCK:
            return stype == SpotType.LARGE
        return False
