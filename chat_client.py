import os
from dotenv import load_dotenv
import socketio

load_dotenv()

import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("已連上聊天室伺服器！")

@sio.event
def message(data):
    print(data)

@sio.event
def disconnect():
    print("與伺服器斷開連線")

def send_loop():
    while True:
        try:
            msg = input()
            sio.send(msg)
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    server_url = os.getenv("CHAT_SERVER_URL")
    sio.connect(server_url) 
    send_loop()
