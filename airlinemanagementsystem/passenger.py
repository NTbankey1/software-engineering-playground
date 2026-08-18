class Passenger:
    def __init__(self, passenger_id: str, name: str, email: str, phone: str) -> None:
        super().__init__()
        self.passenger_id: str = passenger_id
        self.name: str = name
        self.email: str = email
        self.phone: str = phone
