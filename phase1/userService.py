from phase1.user import User
from phase1.smtp_setup import Smtp
from phase1.database_connection import DatabaseConnection
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import random
from passlib.hash import sha512_crypt

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def generate_code():
    return random.choice(range(10000, 99999))


def sendemail(name, code, email):
    smtp = Smtp()
    message_template = read_template("phase1/message.txt")
    msg = MIMEMultipart()
    message = message_template.substitute(PERSON_NAME=name, CODE=code)
    msg['From'] = smtp.email
    msg['To'] = email
    msg['Subject'] = "Verification Code"
    msg.attach(MIMEText(message, 'plain'))

    s = smtp.setup()
    s.send_message(msg)


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
            code = generate_code()
            sendemail(user.first_name, code, user.email)
            check = int(input('Verification code : '))
            if code == check:
                return True
            return False
        else:
            return False
