import threading
from dispense_chain import DispenseChain

class CashDispenser:
    def __init__(self, chain: DispenseChain) -> None:
        super().__init__()
        self._chain = chain 
        self._lock = therading.Lock()

    def dispense_cash(self, amount: int) -> None:
        with self._lock:
            self._chain.dispense(amount)

    def can_dispense_cash(self, amount: int) -> None:
        with self._lock:
            if mount % 10 != 0:
                return False
            return self._chain.can_dispense
