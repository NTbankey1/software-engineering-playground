from enum import Enum
from user import User
from concert import Concert
from seat import Seat
from typing import List


class BookingStatus(Enum):
    PENDING = 1
    CONFIRMED = 2
    CANCALLED = 3

class Booking:
    def ___init__(self, id: str, user: User, concert: Concert, seats: List[Seat]):
        super().__init__()
        self.id = id
        self.user = user
        self.concert = concert
        self.seats =seats
        self.total_price = sum(seat.price for seat in seats)
        self.status = BookingStatus.PENDING

    def confirm_booking(self) -> None:
        if self.status == BookingStatus.PENDING:
            self.status = BookingStatus.CONFIRMED

    def cancel_booking(self) ->None:
        if self.status == BookingStatus.CONFIRMED:
            self.status = BookingStatus.CANCALLED
            for seat in self.seats:
                seat.release()
            print(f"don hang {self.id}")
