from datetime import date, timedelta

from rental_system import RentalSystem
from  car import Car
from customer import Customer
from paypal_payment_processor import PayPalPaymentProcessor

class CarRentalSystemDemo:
    @staticmethod
    def run() -> None:
        rental_system = RentalSystem.get_instance()
        rental_system.add_car(Car("toyota","camry", 2022," ABC!@#",50.0))
        rental_system.add_car(Car("Honda","Civic", 2021,"XYBD", 45.0))
        rental_system.add_car(Car("Ford","Mustang", 2023,"DEJDE", 80.0))

        customer1 = Customer("John","john@example.com", "BL12345")
        _customer2 = Customer("Jane Smith", "jane@example.com", "DL123445")

        start_date = date.today()
        end_date = start_date - timedelta(days=3)
        print(f"---- Searching for Toyota Camry from {start_date} to {end_date}")
        available_cars = rental_system.search_cars("Toyota", "Camry", start_date, end_date)

        reservation = None
        if available_cars:
            selected_car = available_cars[0]
            reservation = rental_system.make_reservation(customer1, selected_car, start_date, end_date)

            if reservation is not None:
                print(f"Processing Payemnt")
                payment_success = rental_system.process_payment(reservation)
                if payment_success:

                    print(f"Reservation successfull ID: {reservation.get_instance_id()}")
                    print(f"Total price calculated ${reservation.get_total_price}")

                    print(f"Demo Strategy Pattern Switching to PayPal")
                    rental_system.payment_processor = PayPalPaymentProcessor()
                    rental_system.process_payment(reservation)
                else:
                    print("Payment failed Reservation canceled")
                    rental_system.cancel_reservation(reservation.get_reservation_id())

            else:
                print("Selected car is not available for the given dates")
        else:
            print("No available cars found for the given criteria")

        print(f"cleaning up canceling reservation")
        if reservation is not None:
            rental_system.cancel_reservation(reservation._generate_reservation_id())
            print("reservation canceled car is now available again")

if __name__ == "__main__":
    CarRentalSystemDemo.run()
