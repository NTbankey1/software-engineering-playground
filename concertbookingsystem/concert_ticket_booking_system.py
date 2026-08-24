from concert import Concert
from typing import Optional, Self, Dict, List
from threading import Lock
from booking import Booking
from datetime import datetime
from user import User
from seat import Seat, SeatStatus, SeatNotAvailableException
import uuid

class ConcertTicketBookingSystem:
    _instance: Optional[Self] = None
    _initialized: bool = False
    concerts: Dict[str, Concert] = {}
    bookings: Dict[str, Booking] = {}
    _lock: Lock = Lock()

    def __new__(cls) -> Self:
        if cls._instance is None:
           cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return
        super().__init__()
        self._initialized = True
        self.concerts: Dict[str, Concert] = {}
        self.bookings:Dict[str, Booking] = {}
        self._lock: Lock = Lock()

    def add_concert(self, concert: Concert ) -> None:
        self.concerts[concert.id] = concert

    def get_concert(self, concert_id: str) -> Optional[Concert]:
        return self.concerts.get(concert_id)

    def seatch(self, artist: str, venue: str, date_time: datetime) -> List[Concert]:
        return [
            concert for concert in self.concerts.values()
            if concert.artist.lower() == artist.lower() and
                concert.venue.lower() == venue.lower() and
                concert.date_time == date_time
        ]

    def book_ticket(self, user: User, concert: Concert, seats: List[Seat]) -> Booking:
        with self._lock:
            for seat in seats:
                if seat.status != SeatStatus.AVAILABLE:
                    raise SeatNotAvailableException(f"ghe{seat.seat_number}")

            for seat in seats:
                seat.book()

            booking_id = self._generate_booking_id()
            booking = Booking(booking_id, user, concert, seats)
            self.bookings[booking_id] = booking

            self._process_payment(booking)
            booking.confirm_booking()
            print(f"don hang {booking.id} da thanh cong {len(booking.seats)}")

            return booking

    def cancel_booking(self, booking_id: str) -> None:
        booking = self.bookings.get(booking_id)
        if booking:
            booking.cancel_booking()
            del self.bookings[booking_id]


    def _process_payment(self, booking: Booking) -> None:
        pass

    def _generate_booking_id(self) -> str:
        return f"BKG{uuid.uuid4()}"
