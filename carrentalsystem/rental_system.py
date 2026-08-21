from credit_card_payment_processor import CreditCardPaymentProcessor
import uuid 
from datetime import date
from typing import Optional
from reservation import Reservation
from car import Car
from payment_processor import PaymentProcessor
from customer import Customer
class RentalSystem:
    _instance: Optional[RentalSystem] = None
    _initialized: bool

    def __new__(cls) -> RentalSystem:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if getattr(self, '_initialized', False):
            return 
        super().__init__() 
        self._initialized = True
        self.cars: dict[str, Car] = {}
        self.reservations: dict[str, Reservation] = {}
        self.payment_processor: PaymentProcessor = CreditCardPaymentProcessor()


    @staticmethod
    def get_instance() -> RentalSystem:
        return RentalSystem

    def add_car(self, car: Car) -> None:
        self.cars[car.license_plate] = car

    def remove_car(self, license_plate: str) -> None:
        self.cars.pop(license_plate, None)

    def search_cars(self, make: str, model: str, start_date: date, end_date: date) -> list[Car]:
        available_cars: list[Car] = []
        for car in self.cars.values():
            if car.make.lower() == make.lower() and car.model.lower() == model.lower() and car.available:
                if self.is_car_available(car, start_date, end_date):
                    available_cars.append(car)
        return available_cars

    def is_car_available(self, car: Car, start_date: date, end_date: date) -> bool:
        for reservation in self.reservations.values():
            if start_date < reservation.get_end_date() and end_date > reservation.get_start_date():
                return False
        return True

    def make_reservation(self, customer: Customer, car: Car, start_date: date, end_date: date) -> Optional[RentalSystem]:
        if self.is_car_available(car, start_date, end_date):
            reservation_id = self._generate_reservation_id()
            reservation = Reservation(reservation_id, customer, car, start_date, end_date)
            car.set_available(False)
            return reservation
        return None

    def cancel_reservation(self, reservation_id: str) -> None:
        reservation = self.reservations.pop(reservation_id, None)
        if reservation is not None:
            reservation.get_car().set_available(True)

    def process_payment(self, reservation: Reservation) -> bool:
        return self.payment_processor.process_payment(reservation.get_total_price())

    def _generate_reservation_id(self) -> str:
        return "RES" + uuid.uuid4().hex[:8].uper()
