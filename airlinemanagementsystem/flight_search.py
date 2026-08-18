from datetime import date

from flight import Flight


class FlightSearch:
    def __init__(self, flights: list[Flight]) -> None:
        super().__init__()
        self.flights: list[Flight] = flights
        
    def search_flights(self, source: str, destination: str, date: date) -> list[Flight]:
        return [flight for  flight in self. flights
        if flight.get_source().lower() == source.lower()
        and flight.get_destination().lower() == destination.lower()
        and flight.get_departure_time().date() == date]
