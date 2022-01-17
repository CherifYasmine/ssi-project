from phase1.database_connection import DatabaseConnection
from passlib.hash import sha512_crypt
from phase1.user import User

class UserService: 
    databaseConnection: DatabaseConnection

    def __init__(self, databaseConnection):
        self.databaseConnection = databaseConnection

    def get_user_by_email(self, email: str):
        query = "SELECT * FROM users where email = %s"
        user_email = (email,)
        cursor = self.databaseConnection.db_connection.cursor()
        cursor.execute(query, user_email)
        return cursor.fetchone()

    def add_user(self, first_name: str, last_name: str, email: str, password: str):
        if self.get_user_by_email(email=email) is None:
            add_user_query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
            values = (first_name, last_name, email, sha512_crypt.hash(password))
            cursor = self.databaseConnection.db_connection.cursor()
            cursor.execute(add_user_query, values)
            self.databaseConnection.db_connection.commit()
        else:
            raise Exception("This user already exists !")

    def login(self, email: str, password: str):
        result = self.get_user_by_email(email=email)
        if result is None:
            return False
        user = User(user=result)
        password_verif = sha512_crypt.verify(password, user.password)
        if password_verif is True:
            return True
        else:
            return False
