import socket
import json

from common import ADDR

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)
data = s.recv(600).decode()
data = json.loads(data)
print(f"Your name: {data["name"]}, your age: {data['age']}. You said us: {data["info"]}. We were surprised..." )