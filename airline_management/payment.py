from enum import Enum


class PaymentStatus(Enum):
    PENDING  = 1
    COMPLETED = 2
    FAILED  = 3
    REFUNDED = 4
    

class Payment:
    def __init__(self, payment_id: str, payment_method: str, amount: float) -> None:
        super().__init__()
        self.payment_id: str = payment_id 
        self.payment_method: str = payment_method
        self.amount: float = amount
        self.status: PaymentStatus = PaymentStatus.PENDING

    def process_payment(self) -> None:
        self.status = PaymentStatus.COMPLETED
