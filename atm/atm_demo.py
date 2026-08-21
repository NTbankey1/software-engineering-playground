from atm import ATM
from operation_type import OperationType
class ATMDemo:
    @staticmethod
    def main() -> None:
        atm = ATM.get_instance()
        print("---scenario 1 Check Balance ---")
        
        atm.insert_card("1234-567-890")
        atm.enter_pin("1234")   
        atm.select_operation(OperationType.CHECK_BALANCE)

        print("\n scenario 2 withdraw cash 570")
        atm.insert_card("1234567")
        atm.enter_pin("12345")
        atm.select_operation(OperationType.WITHDRAW_CASH, 570)

        print("\n Scenario 3 Deposit Cash 200")
        atm.insert_card("3456")
        atm.enter_pin("1234")
        atm.select_operation(OperationType.DEPOSIT_CASH, 200)

        print(" Scenario 4 Re-check-balance")
        atm.insert_card("31092301")
        atm.enter_pin("31312")
        atm.select_operation(OperationType.CHECK_BALANCE)

if __name__ == "__main__":
    ATMDemo.main()
