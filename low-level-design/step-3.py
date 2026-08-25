from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, message: str):
        pass


class Customer(Observer):

    def update(self, message: str):
        print(f"Customer nhận: {message}")


class Restaurant(Observer):

    def update(self, message: str):
        print(f"Restaurant nhận: {message}")


class Driver(Observer):

    def update(self, message: str):
        print(f"Driver nhận: {message}")


class Order:

    def __init__(self):
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify(self, message: str):
        for observer in self.observers:
            observer.update(message)

    def change_status(self, status: str):
        print(f"Order → {status}")
        self.notify(f"Đơn hàng chuyển sang {status}")

order = Order()

customer = Customer()
restaurant = Restaurant()
driver = Driver()

order.add_observer(customer)
order.add_observer(restaurant)
order.add_observer(driver)

order.change_status("DELIVERING")
