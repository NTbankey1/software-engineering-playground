import datetime
from typing import Optional
from threading import Lock

from booking import Booking
from flight import Flight
from passenger import Passenger
from seat import Seat



class BookingManager:
    _instance: Optional[BookingManager] = None
    _lock = Lock()
    _initialized: bool

    def __new__(cls) -> BookingManager:
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if getattr(self, '_initialized', False):
            return 
        super().__init__()
        self._initialized = True
        self.bookings: dict[str, Booking] = {}
        self.booking_counter: int = 0

    def create_booking(self, flight: Flight, passenger: Passenger, seat: Seat, price: float) -> Booking:
        booking_number = self._generate_booking_number()
        booking = Booking(booking_number, flight, passenger, seat, price)
        with self._lock:
            self.bookings[booking_number] = booking
        return booking

    def cancel_booking(self, booking_number: str) -> None:
        with self._lock:
            booking = self.bookings.get(booking_number)
            if booking:
                booking.cancel()

    def _generate_booking_number(self) -> str:
        self.booking_counter += 1
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return f"BKG{timestamp} {self.booking_counter:06d}"
