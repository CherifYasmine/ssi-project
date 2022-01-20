import socket
import json
import threading
import sys
import time


class Server:
    def __init__(self, ADDR):
        self.ADDR = ADDR
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)
        self.active_users = {}  # {username : [conn, pub_key]}

    def send_list_active_users(self):
        user_info = {user: self.active_users[user][1] for user in self.active_users}
        users = {"users": user_info}
        for user, info in self.active_users.items():
            info[0].send(json.dumps(users).encode())

    def send_message(self, receiver, msg, sender, sign):
        data = {"sender": sender, "msg": msg, "sign": sign}
        conn = self.active_users[receiver][0]
        conn.send(json.dumps(data).encode())

    def disconnect_client(self, username, client):
        print(f"[DISCONNECTING] {username}")
        client.send("DISCONNECTING".encode())
        client.close()
        del self.active_users[username]
        self.send_list_active_users()

    def init_data(self, client):
        data = client.recv(1024).decode()
        data = json.loads(data)
        self.active_users[data["username"]] = [client, data["pubkey"]]
        self.send_list_active_users()
        return data["username"]

    def listen_client(self, conn, addr):
        username = self.init_data(conn)
        while True:
            msg = conn.recv(1024).decode()
            data = json.loads(msg)
            if data["msg"] == "!DISCONNECT":
                self.disconnect_client(username, conn)
            else:
                print(f"[MESSAGE] {data}")
                self.send_message(data["receiver"], data["msg"], data["sender"], data["sign"])

    def run(self):
        print("[STARTING] server is starting...")
        try:
            self.server.listen()
            print(f"[LISTENING] Server is listening on {ADDR}")
            while True:
                conn, addr = self.server.accept()
                thread = threading.Thread(target=self.listen_client, args=(conn, addr))
                thread.start()
                time.sleep(1)
                print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
                print(f"[USERS] {list(self.active_users.keys())}")
        except Exception as e:
            # print(e)
            self.server.close()


IP = socket.gethostbyname(socket.gethostname())
PORT = int(sys.argv[1])
ADDR = (IP, PORT)

server = Server(ADDR)
server.run()