


class Card:
    def __init__(self, card_number: str, pin: str) -> None:
        super().__init__()
        self._card_number = card_number
        self._pin = pin
    
    @property
    def card_number(self) -> str:
        return self._card_number
    
    @property 
    def pin(self) -> str:
        return self._pin

    def __repr__(self) -> str:
        return f"card{self._card_number}"
