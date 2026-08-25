from enum import Enum


class OrderStatus(Enum):
    PENDING = 1
    CONFIRMED = 2
    DELIVERING = 3
    COMPLETED = 4
    CANCELLED = 5


class Customer:
    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name


class Food:
    def __init__(self, food_id: str, name: str, price: float):
        self.food_id = food_id
        self.name = name
        self.price = price


class Restaurant:
    def __init__(self, restaurant_id: str, name: str):
        self.restaurant_id = restaurant_id
        self.name = name
        self.foods = []


class Driver:
    def __init__(self, driver_id: str, name: str):
        self.driver_id = driver_id
        self.name = name


class Order:
    def __init__(
        self,
        order_id: str,
        customer: Customer,
        restaurant: Restaurant
    ):
        self.order_id = order_id
        self.customer = customer
        self.restaurant = restaurant

        self.foods = []
        self.driver = None
        self.status = OrderStatus.PENDING
customer = Customer("C001", " Bao")
restaurant = Restaurant("R001","Python Restaurant")

food = Food("F001","Burger", 5.0)
driver = Driver("D001","John")

restaurant.foods.append(food)
order = Order("C001", customer, restaurant)

order.foods.append(food)
order.driver = driver

print(order.order_id)
print(order.customer.name)
print(order.restaurant.name)
print(order.foods[0].name)
print(order.driver.name)
print(order.status)
