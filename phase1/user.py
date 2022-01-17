class User:
    id: int
    email: str
    first_name: str
    last_name: str
    password: str

    def __init__(self, user):
        self.id = user[0]
        self.first_name = user[1]
        self.last_name = user[2]
        self.email = user[3]
        self.password = user[4]