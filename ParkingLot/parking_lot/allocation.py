from typing import List, Optional
from .floor import ParkingFloor
from .models import ParkingSpot
from .enums import VehicleType

class AllocationService:
    """Deterministically picks first compatible free spot across floors."""
    def __init__(self, floors: List[ParkingFloor]):
        self.floors = sorted(floors, key=lambda f: f.floor_id)

    def find_spot(self, vtype: VehicleType) -> Optional[ParkingSpot]:
        for floor in self.floors:
            spot = floor.find_free_spot(vtype)
            if spot:
                return spot
        return None
