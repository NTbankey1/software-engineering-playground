from typing import Dict, Optional
from card import Card
from account import Account


class BankService:
    def __init__(self) -> None:
        super().__init__()
        self._acounts: Dict[str, Account] = {}
        self._cards: Dict[str, Card] = {}
