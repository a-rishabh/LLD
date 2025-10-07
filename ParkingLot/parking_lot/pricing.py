from datetime import datetime
from abc import ABC, abstractmethod
import math

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, entry: datetime, exit: datetime) -> float:
        pass


class FlatRatePricing(PricingStrategy):
    """Same price per hour, rounded up."""
    def __init__(self, rate_per_hour: float = 10.0):
        self.rate = rate_per_hour

    def calculate_fee(self, entry: datetime, exit: datetime) -> float:
        hours = max(1, math.ceil((exit - entry).total_seconds() / 3600))
        return hours * self.rate


class HourlySlabPricing(PricingStrategy):
    """First hour high, then reduced rate."""
    def __init__(self, first_hour_rate: float = 10.0, later_hour_rate: float = 5.0):
        self.first = first_hour_rate
        self.later = later_hour_rate

    def calculate_fee(self, entry: datetime, exit: datetime) -> float:
        hours = max(1, math.ceil((exit - entry).total_seconds() / 3600))
        if hours <= 1:
            return self.first
        return self.first + (hours - 1) * self.later
