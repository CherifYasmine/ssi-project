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
        email = str(input("Entrer votre email: "))
        password = str(input("Entrer votre mot de passe: "))
        password_confirmation = str(input("confirm your password : "))
        # password = getpass.getpass("Enter your password: ")
        # password_confirmation = getpass.getpass("Confirm your password: ")
        email_regex = r"\b[A-Za-z0-9]+\.[A-Za-z0-9]+@insat.ucar.tn\b"
        if (re.fullmatch(email_regex, email) and password == password_confirmation and len(password) > 6):
            verif = True
    first_name, last_name = email.split("@")[0].split(".")
    try:
        userService.add_user(first_name=first_name, last_name=last_name, email=email, password=password)
        print("Utilisateur créé avec succés")
    except:
        print("Cet utilisateur existe déjà, essayer de nouveau!")
        sign_up(userService=userService)




def login(userService: UserService):
    email = None
    password = None
    while email is None and password is None:
        email = str(input("Entrer votre email: "))
        password = str(input("Entrer votre mot de passe: "))
        # password = getpass.getpass("Enter your password: ")

    loggedIn = userService.login(email=email, password=password)
    if loggedIn is True:
        print("Login avec succès!")
    else:
        print("Verifier vos informations!")
