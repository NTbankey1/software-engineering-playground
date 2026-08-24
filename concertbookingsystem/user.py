

class User:
    def __init__(self, user_id: str, name: str, email: str):
        super().__init__()
        self.id = user_id
        self.name =name
        self.email = email
