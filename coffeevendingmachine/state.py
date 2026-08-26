
from typing import TYPE_CHECKING

from abc import ABC, abstractmethod


if TYPE_CHECKING:
    from coffee_vending_machine import CoffeeVendingMachine
    from coffee import Coffee

class VendingMachineState(ABC):
    @abstractmethod
    def select_coffee(self, machine: 'CoffeeVendingMachine', coffee: 'Coffee') -> None:
        pass

    @abstractmethod
    def insert_money(self, machine: 'CoffeeVendingMachine', amount: int) -> None:
        pass

    @abstractmethod
    def dispense_coffee(self, machine: 'CoffeeVendingMachine') -> None:
        pass

    @abstractmethod
    def cancel(self, machine: 'CoffeeVendingMachine') -> None:
        pass


class ReadyState(VendingMachineState):
    def select_coffee(self, machine: 'CoffeeVendingMachine', coffee: 'Coffee') -> None:
        machine.set_selected_coffee(coffee)
