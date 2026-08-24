from concert_ticket_booking_system import ConcertTicketBookingSystem
from typing import List
from seat import Seat, SeatType, SeatStatus
from concert import Concert
from datetime import datetime
from user import User

class ConcerTicketBookingSystemDemo:
    @staticmethod
    def run() -> None:
        booking_system = ConcertTicketBookingSystem()
        concert1_seats = ConcerTicketBookingSystemDemo._generate_seats(100)
        concert1 = Concert("C002","Aritist 1", "Venue 1", datetime.now().replace(day=10, hour=20, minute=0, second=0, microsencond=0), concert1_seats)
        booking_system.add_concert(concert1)

        user1 = User("U001","john doe", "johan@example.com")
        search_results = booking_system.search_concerts("Arits1"," Venue", concert1.date_time)
        print("search results")
        for concert in search_results:
            print(f"concert{concert.artist} at {concert.venue}")

        selected_seats1 = ConcerTicketBookingSystemDemo._select_seats(concert1, 3)
        booking1 = booking_system.book_ticket(user1, concert1, selected_seats1)



    @staticmethod
    def _generate_seats(number_of_seats: int) -> List[Seat]:
        seats = []
        for i in range(1, number_of_seats + 1):
            seat_number = f"S{i}"
            seat_type = SeatType.VIP if i <= 10 else SeatType.PREMIUM if i <= 30 else SeatType.REGULAR
            price = 100.0 if seat_type == SeatType.VIP else 75.0 if seat_type == SeatType.PERMIUM else 50.0
            seats.append(Seat(seat_number, seat_number, seat_type, price))
        return seats

    @staticmethod
    def _select_seats(concert: Concert, number_of_seats: int) -> List[Seat]:
        available_seats = [seat for seat in concert.seats if seat.status == SeatStatus.AVAILABLE]
        return available_seats[:number_of_seats]

if __name__ == " __main__":
   ConcerTicketBookingSystemDemo.run()
