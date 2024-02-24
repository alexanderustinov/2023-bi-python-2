import socket
import pickle

from common import ADDR

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)
data = s.recv(600)
data = pickle.loads(data)
print(f'Your name: {data.name}, your age: {data.age}. You said us: "{data.inf()}". We were surprised...' )