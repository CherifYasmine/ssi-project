import mysql.connector


class DatabaseConnection:
    db_connection = None

    def __init__(self, hostname, user, password, database):
        try:
            self.db_connection = mysql.connector.connect(host=hostname, user=user, password=password, database=database)
            print("Connected to Database successfully")
        except mysql.connector.Error as error:
            print("Error Database Connection")

    def __str__(self):
        return "Database connection object"
