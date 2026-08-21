from __future__ import annotations
from datetime import date
from car import Car
from customer import Customer

class Reservation:
    def __init__(self, reservation_id: str, customer: Customer, car: Car, start_date: date, end_date: date) -> None:
        super().__init__()
        self.reservation_id: str = reservation_id
        self.customer: Customer = customer
        self.car: Car = car
        self.start_date: date = start_date
        self.end_date: date = end_date
        self.total_price: float = self.calculate_total_price()

    def calculate_total_price(self) -> float:
        days_rentad = (self.end_date - self.start_date).days + 1
        return self.car.rental_price_per_day * days_rentad

    def get_start_date(self) -> date:
        return self.start_date

    def get_end_date(self) -> date:
        return self.end_date

    def get_car(self) -> Car:
        return self.car

    def get_total_price(self) -> float:
        return self.total_price

    def get_reservation_id(self) -> str:
        return self.reservation_id
