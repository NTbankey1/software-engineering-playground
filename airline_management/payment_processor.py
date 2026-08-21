from typing import Optional
from threading import Lock

from payment import Payment 


class PaymentProcessor:
    _instance: Optional[PaymentProcessor] = None
    _lock = Lock()
    _initialized: bool

    def __new__(cls) -> PaymentProcessor:
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None: 
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if getattr(self, '_initialized', False):
            return 
        super().__init__()
        self._initialized = True

    def process_payment(self, payment: Payment) -> None:
        payment.process_payment()
