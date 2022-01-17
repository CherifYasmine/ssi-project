import os

from python-dotenv import load_dotenv
from phase1.database_connection import DatabaseConnection
from phase1.userService import UserService
from phase1 import authentification
load_dotenv(".env")
if __name__ == "__main__":
    choice = None
    DB_HOSTNAME: str = os.environ.get("DB_HOSTNAME")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
    DB_DATABASE: str = os.environ.get("DB_DATABASE")
    conn = DatabaseConnection(
        hostname=DB_HOSTNAME,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE,
    )
    userService = UserService(databaseConnection=conn)
    while choice != 4:
        choice = int(
            input(
                "Enter your choice: \n"
                "1. Sign up.\n"
                "2. Login.\n"
                "3. Phase3.\n"
                "4. Quit.\n"
            )
        )

        if choice == 1:
            authentification.sign_up(userService=userService)
        elif choice == 2:
            authentification.login(userService=userService)
        elif choice == 3:
            print()
