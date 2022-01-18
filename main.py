import os
from Crypto.Random import get_random_bytes
from dotenv import load_dotenv
from phase1.database_connection import DatabaseConnection
from phase1.userService import UserService
from phase1 import authentification
from phase2 import encode_decode
from phase2 import hash
from phase2 import crypt
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
                "3. Menu.\n"
                "4. Quit.\n"
            )
        )

        if choice == 1:
            authentification.sign_up(userService=userService)
        elif choice == 2:
            authentification.login(userService=userService)
        elif choice == 3:
            choice_menu = int(input(
                    "Enter your choice: \n"
                    "1. Codage et décodage\n"
                    "   1- Codage \n"
                    "   2- Decodage \n"
                    "2. Hashage d'un message \n"
                    "   1- MD5 \n"
                    "   2- SHA1 \n"
                    "   3- SHA256 \n"
                    "3. Craquage d'un message haché \n"
                    "   1- MD5 \n"
                    "   2- SHA1 \n"
                    "   3- SHA256 \n"
                    "4. Chiffrement et déchiffrement symétrique d'un message \n"
                    "   1- DES \n"
                    "   2- AES256 \n"
                    "5. Chiffrement et déchiffrement asymétrique d'un message \n"
                    "   1- RSA \n"
                    "   2- elgamal \n"
                    "6. Communication sécurisé entre deux clients (ChatRoom)\n"
                    "7. Quit \n"
                ))
            if choice_menu == 11:
                message = input(" entrer votre message ")
                encode_decode.encode(message)
            if choice_menu == 12:
                message = input(" entrer votre message ")
                encode_decode.decode(message)
            if choice_menu == 21:
                hash.md5()
            if choice_menu == 22:
                hash.sha1()
            if choice_menu == 23:
                hash.sha256()
            if choice_menu == 41:
                choice_crypt = int(input("1. chiffrement \n" "2. Dechiffrement \n"))
                key = get_random_bytes(16)
                if choice_crypt == 1:
                    crypt.des_crypt(key)
                if choice_crypt == 2:
                    crypt.des_decrypt(key)
            if choice_menu == 42:
                key = get_random_bytes(16)
                choice_crypt = int(input("1. chiffrement \n" "2. Dechiffrement \n"))
                if choice_crypt ==1:
                    crypt.aes256_crypt(key)
                if choice_crypt == 2:
                    crypt.aes256_decrypt(key)





        elif choice == 4:
            exit()




