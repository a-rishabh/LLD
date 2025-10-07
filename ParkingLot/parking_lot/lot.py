from datetime import datetime
from typing import Dict
from .floor import ParkingFloor
from .models import Vehicle, Ticket
from .pricing import PricingStrategy
from .allocation import AllocationService
from .errors import NoCompatibleSpotError

class ParkingLot:
    """Main orchestrator for entry/exit."""
    def __init__(self, name: str, floors: list[ParkingFloor], pricing: PricingStrategy):
        self.name = name
        self.floors = floors
        self.pricing = pricing
        self.tickets: Dict[str, Ticket] = {}
        self.allocation = AllocationService(floors)

    def park(self, vehicle: Vehicle) -> Ticket:
        spot = self.allocation.find_spot(vehicle.vtype)
        if not spot:
            raise NoCompatibleSpotError("Lot full for this vehicle type.")
        floor = next(f for f in self.floors if f.floor_id == spot.floor)
        assigned = floor.assign_vehicle(vehicle)
        ticket_id = f"{vehicle.license_no}-{datetime.utcnow().timestamp():.0f}"
        ticket = Ticket(ticket_id, vehicle, assigned.spot_id, datetime.utcnow())
        self.tickets[ticket_id] = ticket
        return ticket

    def unpark(self, ticket_id: str) -> float:
        ticket = self.tickets.get(ticket_id)
        if not ticket:
            raise ValueError("Invalid ticket ID.")
        ticket.close()
        exit_time = ticket.exit_time
        fee = self.pricing.calculate_fee(ticket.entry_time, exit_time)
        # find the floor & free spot
        for floor in self.floors:
            try:
                floor.free_spot(ticket.spot_id)
                break
            except Exception:
                continue
        del self.tickets[ticket_id]
        return fee
