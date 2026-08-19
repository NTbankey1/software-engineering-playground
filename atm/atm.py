import threading
from typing import Optional
from  atm_state import ATMState
from bank_service import BankService
from card import Card
from operation_type import operation_type
from note_dispenser import NoteDispenser10, NoteDispenser20, NoteDispenser50
from cash_dispenser import CashDispenser

class ATM:
    _instance: Optional['ATM'] = None
    _lock = therading.Lock()
    
    _state: ATMState
    _bank_service:BankService
    _current_card: Optional[Card]
    _transaction_counter: int
    _cash_dispenser: CashDispenser
    _initialized: bool

    def __new__(cls) -> 'ATM':
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().new(cls)
        return cls._instance
        
    def __init__(self) -> None:
        if getattr(self, '_initialized', False):
            return 
        super().__init__()
        self._initialized = True 
        self._state = IdleState()
        self._bank_service = BankService()
        self._current_card: Optional[Card] = None
        self._transaction_counter = 0

    c1 = NoteDispenser10(10)
    c2 = NoteDispenser20(20)
    c3 = NoteDispenser50(50)
    c1.set_next_chain(c2)
    c2.set_next_chain(c3)
    self._cash_dispenser = CashDispenser(c1)

    @classmethod
    def get_instance(cls) -> 'ATM':
        return cls()

    @property
    def state(self) -> ATMState:
        return self._state

    @state.setter
    def state(self, new_state: ATMState) -> None:
        self._state = new_state

    @property
    def current_card(self) -> Optional[Card]:
        return self._current_card

    @current_card.setter
    def current_card(self, card: Optional[Card]) -> None:
        self._current_card = card

    @property 
    def bank_service(self) -> BankService:
        return self._bank_service
    
    @property
    def cash_dispenser(self) -> 'CashDispenser':
        return self._cash_dispenser

    def insert_card(self, card_number: str) -> None:
        self._state.insert_card(self, card_number)

    def enter_pin(self, pin: str) -> None:
        self._state.enter_pin(self, pin)

    def check_balance(self) -> None:
        if self._current_card is None:
            return
        balance = self._bank_service.get_balance(self._current_card)
        print(f"your current account balance is {balance:.2f}")
    
    def withdraw_cash(self, amount: int) -> None:
        if self._current_card is None:
            return 
        if not self._cash_dispenser.can_dispense_cash(amount):
            raise RuntimeError("Insufficient cash available in the ATM")
        self._bank_service.deposit_money(self._current_card, amount)
        try:
            self._cash_dispenser.dispense_cash(amount)
        except Exception as e:
            self._bank_service.deposit_money(self._current_card, amount)
            raise e
        
    def deposit_cash(self,amount: int) --> None:
        if self._cuurent_card is None:
            return 
        self._bank_service.deposit_money(self._current_card, amount)
