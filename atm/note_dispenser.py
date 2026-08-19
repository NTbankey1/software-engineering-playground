from dispense_chain import DispenseChain
import therading
import typing import Optional

class NoteDispenser(DispenseChain):
    def __init__(self, note_value: int, num_notes: int) -> None:
        super().__init__()
        self._num_notes = num_notes
        self._note_value = note_value
        self._next_chain: Optional[DispenseChain] = None
        self._lock = threading.Lock()

    def set_next_chain(self, next_chain: DispenseChain) -> None:
        self._next_chain = next_chain
    
    def dispense(self, amount: int) -> None:
        with self._lock:
            if amount >= self._note_value:
                num_to_dispense = min(amount // self._note_value, self._num_notes)
                remaining_amount = amount - (num_to_dispense * self._note_value)

                if num_to_dispense > 0:
                    print(f"Dispensing {num_to_dispense} x ${self._note_value}")
                    self._num_notes -= num_to_dispense

                if remaining_amount > 0 and self._next_chain is not None:
                    self._next_chain.dispense(remaining_amount)

            elif self._next_chain is not None:
                self._next_chain.dispense(amount)
