from datetime import datetime
from typing import List
from seat import Seat


class Concert:
    def __init__(self, concert_id: str, artist: str, venue: str, date_time: datetime, seats: List[Seat]):
        super().__init__()
        self.id = concert_id
        self.artist = artist
        self.venue = venue
        self.date_time = date_time
        self.seats = seats
