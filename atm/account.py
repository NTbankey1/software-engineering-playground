import threading
from typing import Dict
from card import Card

class  Account:
    def __init__(self, account_number: str, balance: float) -> None:
        super().__init__()
        self._account_number =account_number
        self._balance = balance 
        self._cards: Dict[str, Card] ={}
        self._lock = threading.Lock()

    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def cards(self) -> Dict[str: Card]:
        return self._cards

    def __repr__(self) -> str:
        return f"Account({self._account_number}, balance=${self._balance:.2f})"

    def deposit(self, amount: float) -> None:
        with self._lock:
            self._balance += amount

    def withdraw(self, amount: float) -> bool:
        with self._lock:
            if self._balance >= amount:
                self._balance -= amount
                return True
            return False
