from atm import ATM

class ATMDemo:
    @staticmethod
    def main() -> None:
        atm = ATM.get_instance()
        print("---scenario 1 Check Balance ---")
        
        atm.insert_card("1234-567-890")
    