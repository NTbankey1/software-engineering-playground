class Aircraft:
    def __init__(self, tail_number: str, model: str, total_seats: int) -> None:
        super().__init__()
        self.tail_number :str = tail_number
        self.model :str = model
        self.total_seats :int = total_seats
