from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes

key1 = get_random_bytes(8)
key2 = get_random_bytes(16)


def des_crypt():
   message = input("entrer votre message : ")
   des = DES.new(key1, DES.MODE_ECB)
   encrypted_text: bytes = des.encrypt(message.encode() + (b" " * (8 - (len(message) % 8))))
   print(encrypted_text.hex())


def des_decrypt():
    message = input("entrer votre message : ")
    des = DES.new(key1, DES.MODE_ECB)
    ciphertext: bytes = des.decrypt(bytes.fromhex(message))
    decrypted_text = ciphertext.decode("utf-8").strip()
    print(decrypted_text)


def aes256_crypt():
    message = input("entrer votre message : ")
    cipher = AES.new(key2, AES.MODE_ECB)
    encrypted_text: bytes = cipher.encrypt(message.encode() + (b" " * (16 - (len(message) % 16))))
    print(encrypted_text.hex())


def aes256_decrypt():
    message = input("entrer votre message : ")
    cipher = AES.new(key2, AES.MODE_ECB)
    ciphertext: bytes = cipher.decrypt(bytes.fromhex(message))
    decrypted_text = ciphertext.decode("utf-8").strip()
    print(decrypted_text)
