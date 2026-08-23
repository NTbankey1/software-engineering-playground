
from typing import Optional, Self, Dict, List
from threading import Lock

from concert import Concert
from booking import Booking
from user import User

class ConcertTicketBookingSystem:
    _instance: Optional[Self] = None
    _initialized: bool = False
    concerts: Dict[str, Concert] = {}
    bookings: Dict[str, Booking] = {}
    _lock: Lock = Lock()

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls
