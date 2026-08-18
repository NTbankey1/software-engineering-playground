from enum import Enum

class SeatStatus(Enum):
    AVAILABLE = 1
    RESERVED  = 2
    OCCUPIED  = 3

class SeatType(Enum):
    ECONOMY         = 1
    PREMIUM_ECONOMY = 2
    BUSINESS        = 3
    FIRST_CLASS     = 4

class Seat:
    def __init__(self, seat_number: str, seat_type: SeatType):
        super().__init__()
        self.seat_number: str = seat_number
        self.seat_type :SeatType   = seat_type
        self.status: SeatStatus     = SeatStatus.AVAILABLE

    def reserve(self):
        self.status = SeatStatus.RESERVED

    def release(self):
        self.status = SeatStatus.AVAILABLE
