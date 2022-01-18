from Crypto.Cipher import DES, AES


def des_crypt(key):
    message = input("entrer votre message : ")
    cipher = AES.new(key, DES.MODE_EAX)
    encrypted_text: bytes = cipher.encrypt(message.encode())
    print(encrypted_text.hex())


def des_decrypt(key):
    return 0


def aes256_crypt(key):
    message = input("entrer votre message : ")
    cipher = AES.new(key, AES.MODE_EAX)
    encrypted_text: bytes = cipher.encrypt(message.encode())
    print(encrypted_text.hex())


def aes256_decrypt(key):
    message = input("entrer votre message : ")
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext: bytes = cipher.decrypt(bytes.fromhex(message))
    print(ciphertext.decode("utf-8").strip())
