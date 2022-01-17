import smtplib
import os
from dotenv import load_dotenv


class Smtp:
    email: str
    password: str
    s: object

    def setup(self):
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(self.email, self.password)
        return s

    def __init__(self):
        load_dotenv("../.env")
        self.email = os.environ.get("EMAIL")
        self.password = os.environ.get("PASSWORD")
        self.s = self.setup(self)


