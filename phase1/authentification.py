import getpass
import re
from phase1.userService import UserService

def sign_up(userService: UserService):
    verif = False
    email = None
    password = None
    first_name = None
    last_name = None
    while not verif:
        email = str(input("Enter your email: "))
        # first_name = str(input("Enter your first name: "))
        # last_name = str(input("Enter your last name: "))
        password = getpass.getpass("Enter your password: ")
        password_confirmation = getpass.getpass("Confirm your password: ")
        email_regex = r"\b[A-Za-z0-9]+\.[A-Za-z0-9]+@insat.ucar.tn\b"
        if (re.fullmatch(email_regex, email) and password == password_confirmation and len(password) > 6 ):
            verif = True
    first_name, last_name = email.split("@")[0].split(".")
    try:
        userService.add_user(first_name=first_name, last_name=last_name, email=email, password=password)
        print("User created successfully!")
    except:
        print("This user already exists, try another user!")
        sign_up(userService=userService)

def login(userService: UserService):
    email = None
    password = None
    while email is None and password is None:
        email = str(input("Enter your email: "))
        password = getpass.getpass("Enter your password: ")

    loggedIn = userService.login(email=email, password=password)
    if loggedIn is True:
        print("Login Successfully!")
    else:
        print("Please verify your credentials!")