from abc import ABC, abstractmethod
from token import OP
from operation_type import OperationType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from atm import ATM


class ATMState(ABC):
    @abstractmethod
    def insert_card(self, _atm: 'ATM', _card_number: str) -> None:
        pass 
    
    @abstractmethod
    def enter_pin(self, _atm: 'ATM', _pin: str) -> None:
        pass

    @abstractmethod
    def select_openration(self, _atm: 'ATM', _op: OperationType, *_args: int) -> None:
        pass

    @abstractmethod
    def eject_card(self, _atm: 'ATM') -> None:
        pass

    
class IdleState(ATMState):
    def insert_card(self, atm: 'ATM', card_number: str) -> None:
        print("\ncard has been inserted")
        card = atm.bank_service.authenticate_card(card_number)
        if card is None:
            self.eject_card(atm)
        else:
            atm.current_card = card
            atm.state = HasCardState()

         
    def enter_pin(self, _atm: 'ATM', _pin: str) -> None:
        print("Error Please insert a card first")

    def select_openration(self, _atm: 'ATM', _op: OperationType, *_args: int) -> None:
        print("Error please insert a card first") 
    
    def eject_card(self, _atm: 'ATM') -> None:
        print("Error: Card not found")

class HasCardState(ATMState):
    def insert_card(self, _atm: 'ATM', _card_number: str) -> None:
        print("Error: A card is already inserted Cannot insert another card")

    def enter_pin(self, atm: 'ATM', pin: str) -> None:
        print("Authenticating pin.....")
        card = atm.current_card
        if card is None:
            return 
        if atm.bank_service.authenticate(card, pin):
            print("Authentication successful")
            atm.state = AuthenticatedState()

        else:
            print("authentication failed incorrenct Pin")
            self.ejcet_card(atm)
    
    def select_operation(self, _atm: 'ATM', _op: OperationType, *_args: int) -> None:
        print("Error please enter your pin first to select an operation")

    def eject_card(self, atm: 'ATM',_card_number: str) -> None:
        print("card has been ")
        atm.current_card = None
        atm.state = IdleState

class AuthenticatedState(ATMState):
    def insert_card(self, _atm: 'ATM', _pin: str) -> None:
        print("error pin has already been entered and authenticated")

    def enter_pin(self, _atm: 'ATM', op: OperationType, *args: int) -> None:
        print("error pin has already been entered and authenticated")

    def select_openration(self, atm: 'ATM', op: OperationType, *args: int) -> None:
        error = None
        if op == OperationType.CHECK_BALANCE:
            atm.check_balance()
        elif op == OperationType.WITHDRAW_CASH:
            if len(args) == 0 or args[0] <= 0:
                error = "Invalid withdrawal amount spencicified"
            else:
                card: atm.current_card
            if card is None:
                return 
            balance = atm.bank_service.get_balance(card)
            amount = args[0]
            if amount > balance:
                error = "insufficient balance"
