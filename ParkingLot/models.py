from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from .enums import VehicleType, SpotType
from .errors import SpotAlreadyOccupiedError, SpotNotOccupiedError

@dataclass(frozen=True)
class Vehicle:
    license_no: str
    vtype: VehicleType

    def __str__(self) -> str:
        return f"{self.vtype.name}:{self.license_no}"

@dataclass
class ParkingSpot:
    spot_id: str
    stype: SpotType
    floor: int
    occupied: bool = field(default=False, init=False)
    vehicle: Optional[Vehicle] = field(default=None, init=False, repr=False)

    def can_fit(self, vehicle: Vehicle) -> bool:
        """Compatibility matrix (expandable)."""
        if vehicle.vtype == VehicleType.BIKE:
            return self.stype in {SpotType.MOTORBIKE, SpotType.COMPACT, SpotType.LARGE}
        if vehicle.vtype == VehicleType.CAR:
            return self.stype in {SpotType.COMPACT, SpotType.LARGE}
        if vehicle.vtype == VehicleType.TRUCK:
            return self.stype in {SpotType.LARGE}
        return False

    def assign(self, vehicle: Vehicle) -> None:
        if self.occupied:
            raise SpotAlreadyOccupiedError(f"Spot {self.spot_id} already occupied")
        if not self.can_fit(vehicle):
            raise ValueError(f"Vehicle {vehicle} incompatible with spot {self.stype.name}")
        self.vehicle = vehicle
        self.occupied = True

    def free(self) -> Vehicle:
        if not self.occupied:
            raise SpotNotOccupiedError(f"Spot {self.spot_id} is not occupied")
        v = self.vehicle  # type: ignore[assignment]
        self.vehicle = None
        self.occupied = False
        return v  # type: ignore[return-value]

@dataclass
class Ticket:
    ticket_id: str
    vehicle: Vehicle
    spot_id: str
    entry_time: datetime
    exit_time: Optional[datetime] = None

    def close(self, when: Optional[datetime] = None) -> None:
        self.exit_time = when or datetime.utcnow()
