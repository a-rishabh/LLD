class ParkingError(Exception):
    """Base error for parking-lot domain."""

class NoCompatibleSpotError(ParkingError):
    """Raised when no compatible spot is available for a vehicle type."""

class SpotAlreadyOccupiedError(ParkingError):
    """Raised when attempting to assign to an occupied spot."""

class SpotNotOccupiedError(ParkingError):
    """Raised when attempting to free an already-free spot."""
