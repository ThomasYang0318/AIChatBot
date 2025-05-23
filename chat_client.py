import os
from dotenv import load_dotenv
import socketio

load_dotenv()

sio = socketio.Client()

@sio.event
def connect():
    print("成功連上聊天室伺服器！")

@sio.event
def message(data):
    print(data)

server_url = os.getenv("CHAT_SERVER_URL")
sio.connect(server_url)  
