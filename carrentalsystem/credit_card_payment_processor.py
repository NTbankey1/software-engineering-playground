from payment_processor import PaymentProcessor

class CreditCradPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"processing credit card payment of ${amount}")
        return True
