from __future__ import annotations
from datetime import datetime, timedelta 
from typing import List

from airline_management_system import AirlineManagementSystem
from passenger import Passenger
from flight import Flight
from  aircraft import Aircraft 
from  seat import Seat, SeatType




class AirlineManagementSystemDemo:
    @staticmethod
    def run() -> None:
        airline_management_system = AirlineManagementSystem()

        passenger1 = Passenger("U001", "John Doe", "John@example.com", "123456789")

        departure_time1 = datetime.now() + timedelta(days=1)
        arrival_time1 = departure_time1 + timedelta(hours=2)
        flight1 = Flight("F001", "Paris", "Tokyo", departure_time1, arrival_time1)

        departure_time2 = datetime.now() + timedelta(days=3)
        arrival_time2 = departure_time2 + timedelta(hours= 5)
        flight2 = Flight("F002", "Paris"," Tokyo", departure_time2, arrival_time2)

        airline_management_system.add_flight(flight1)
        airline_management_system.add_flight(flight2)

        aircraft1 = Aircraft("A001", "Boeing 747", 300)
        aircraft2 = Aircraft("A002", "AIrbus A380", 500)
        airline_management_system.add_aircraft(aircraft1)
        airline_management_system.add_aircraft(aircraft2)

        search_date = datetime.now().date() + timedelta(days=1)
        search_results: List[Flight] = airline_management_system.search_flights("New York", "London", search_date)
        
        print("search Results:")
        for flight in search_results:
            print(f"flight: {flight.flight_number} - {flight.source} to {flight.destination}")

        seat = Seat("25A", SeatType.ECONOMY)
        booking = airline_management_system.book_flight(flight1, passenger1, seat, 100)
        if booking:
            print(f"booking successful booking ID { booking.booking_number}")
        else:
            print("Booking cancelled")

    @staticmethod
    def demo_main() -> None:
        AirlineManagementSystemDemo.run()

if __name__ == "__main__":
    AirlineManagementSystemDemo.run()
