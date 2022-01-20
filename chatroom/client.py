import socket
import json
import rsa
import os
import threading
import sys


class Client:
    DISCONNECT_MESSAGE = "!DISCONNECT"
    HASH_METOD = "MD5"

    def __init__(self, ADDR, username):
        self.ADDR = ADDR
        self.username = username
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.active_users = {}
        self.generate_key()

    def generate_key(self):
        try:
            with open(f'{self.username}/priv.key', 'rb') as f:
                priv_file_content = f.read()
            self.privkey = rsa.PrivateKey.load_pkcs1(priv_file_content)
        except IOError:
            os.mkdir(self.username)
            (self.pubkey, self.privkey) = rsa.newkeys(512)
            with open(f'{self.username}/pub.key', 'wb') as f:
                f.write(self.pubkey.save_pkcs1())
            with open(f'{self.username}/priv.key', 'wb') as f:
                f.write(self.privkey.save_pkcs1())
        finally:
            with open(f'{self.username}/pub.key', 'rb') as f:
                pub_file_content = f.read()
            self.pubkey = pub_file_content.decode()

    def digital_signature(self, msg):
        sign = rsa.sign(msg, self.privkey, self.HASH_METOD)
        return sign.hex()  # sign

    def verify_sign(self, msg, sign, sender):
        pubkey_send = rsa.key.PublicKey.load_pkcs1(self.active_users[sender])
        try:
            used_hash = rsa.verify(msg, bytes.fromhex(sign), pubkey_send)
            return True
        except rsa.VerificationError:
            return False

    def disconnection(self):
        data = {"sender": self.username, "receiver": "disconnect", "msg": self.DISCONNECT_MESSAGE}
        self.client.send(json.dumps(data).encode())

    def send_broadcast(self, msg):
        for receiver in self.active_users:
            self.send(receiver, msg)

    def send(self, receiver, msg):
        pubkey_recv = rsa.key.PublicKey.load_pkcs1(self.active_users[receiver])
        crypto = rsa.encrypt(msg, pubkey_recv)
        data = {"sender": self.username, "receiver": receiver, "msg": crypto.hex(), "sign": self.digital_signature(msg)}
        self.client.send(json.dumps(data).encode())

    def update_users(self, users):
        del users[self.username]
        self.active_users = users

    def init_data(self):
        data = {"username": self.username, "pubkey": self.pubkey}
        self.client.send(json.dumps(data).encode())

    def listen(self):
        self.init_data()
        while True:
            data = self.client.recv(1024).decode()
            data = json.loads(data)
            if "users" in data.keys():
                self.update_users(data["users"])
            else:
                crypto = bytes.fromhex(data["msg"])
                msg = rsa.decrypt(crypto, self.privkey).decode()
                if self.verify_sign(msg.encode(), data["sign"], data["sender"]):
                    print(f"\n[NEW MESSAGE VERIFIED] {data['sender']}: {msg} \nMessage: ", end="")
                else:
                    print("[MESSAGE NOT VERIFIED] You received a message not verified \nMessage: ", end="")

    def run(self):
        try:
            print(f"[CONNECTION] Starting connection to {ADDR}")
            self.client.connect(self.ADDR)
            thread = threading.Thread(target=self.listen)
            thread.start()
            while True:
                msg = input("Message: ")
                if msg == self.DISCONNECT_MESSAGE:
                    self.disconnection()
                    break;
                print(f"\n[ACTIVE USERS] {list(self.active_users.keys()) + ['broadcast']}")
                receiver = input("Receiver: ")
                if receiver not in list(self.active_users.keys()) + ["broadcast"]:
                    print(f"not a valid username")
                    continue
                if receiver == "broadcast":
                    self.send_broadcast(msg.encode())
                else:
                    self.send(receiver, msg.encode())
        except Exception as e:
            # print(e)
            pass


IP = socket.gethostbyname(socket.gethostname())
PORT = int(sys.argv[1])
ADDR = (IP, PORT)

username = input("Insert username: ")
client = Client(ADDR, username)
client.run()
