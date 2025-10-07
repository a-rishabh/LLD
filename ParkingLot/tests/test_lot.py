from parking_lot.lot import ParkingLot
from parking_lot.floor import ParkingFloor
from parking_lot.models import ParkingSpot, Vehicle
from parking_lot.enums import VehicleType, SpotType
from parking_lot.pricing import FlatRatePricing

def build_lot():
    floors = []
    for i in range(1, 3):
        spots = [
            ParkingSpot(f"F{i}S1", SpotType.MOTORBIKE, i),
            ParkingSpot(f"F{i}S2", SpotType.COMPACT, i),
            ParkingSpot(f"F{i}S3", SpotType.LARGE, i),
        ]
        floors.append(ParkingFloor(i, spots))
    return ParkingLot("DowntownLot", floors, FlatRatePricing(10))

def test_full_flow():
    lot = build_lot()
    v1 = Vehicle("MN-123", VehicleType.CAR)
    t1 = lot.park(v1)
    assert t1.ticket_id in lot.tickets
    fee = lot.unpark(t1.ticket_id)
    assert fee >= 10
    assert t1.ticket_id not in lot.tickets
