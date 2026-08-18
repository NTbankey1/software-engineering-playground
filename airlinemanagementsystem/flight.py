from datetime import datetime

from seat import Seat

class Flight:
    def __init__(self, flight_number: str, source: str, destination: str, departure_time: datetime, arrival_time: datetime) -> None:
        super().__init__()
        self.flight_number: str = flight_number 
        self.source :str = source 
        self.destination: str = destination
        self.departure_time: datetime = departure_time
        self.arrival_time: datetime = arrival_time
        self.available_seats: list[Seat] = []

    def get_source(self) -> str:
        return self.source

    def get_departure_time(self) -> datetime:
        return self.departure_time

    def get_destination(self) -> str:
        return self.destination
