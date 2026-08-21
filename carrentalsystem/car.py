
class Car:
    def __init__(self, make: str, model: str, year: int, license_plate: str, rental_price_per_day: float) -> None:
        super().__init__()
        self.make: str = make
        self.model: str = model
        self.year: int = year
        self.license_plate: str = license_plate 
        self.rental_price_per_day: float = rental_price_per_day
        self.available: bool = True

    def get_rental_price_per_day(self) -> float:
        return self.rental_price_per_day

    def get_license_plate(self) -> str:
        return self.license_plate

    def get_make(self) -> str:
        return self.make

    def get_model(self) ->  str:
        return self.model

    def get_year(self) -> int:
        return self.year

    def is_available(self) -> bool:
        return self.available

    def set_available(self, available: bool) -> None:
        self.available = available
