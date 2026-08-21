class Customer:
    def __init__(self, name: str, contact_info: str, drivers_license_number: str) -> None:
        super().__init__()
        self.name: str = name
        self.contact_info: str = contact_info
        self.drivers_license_number: str = drivers_license_number
