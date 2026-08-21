
from enum import Enum
from flight import Flight
from passenger import Passenger
from seat import Seat

class BookingStatus(Enum):
    CONFIRMED = 1
    CANCELLED = 2
    PENDING   = 3
    EXPIRED   = 4

class Booking:
    def __init__(self, booking_number: str, flight: Flight, passenger: Passenger, seat: Seat, price: float) -> None:
        super().__init__()
        self.booking_number: str = booking_number 
        self.flight: Flight = flight
        self.passenger: Passenger = passenger
        self.seat: Seat = seat
        self.price: float = price
        self.status: BookingStatus = BookingStatus.CONFIRMED
        
    def cancel(self) -> None:
        self.status = BookingStatus.CANCELLED
