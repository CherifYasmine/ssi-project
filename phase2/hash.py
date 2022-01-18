import hashlib
from phase2 import encode_decode

def md5():
    message = input('entrer votre message : ')
    print(hashlib.md5(message.encode()).hexdigest())


def sha1():
    message = input('entrer votre message : ')
    print(hashlib.sha1(message.encode()).hexdigest())


def sha256():
    message = input('entrer votre message : ')
    print(hashlib.sha256(message.encode()).hexdigest())