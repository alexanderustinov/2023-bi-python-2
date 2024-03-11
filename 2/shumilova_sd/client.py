import socket
import pickle
from common import ADDR

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)
data = pickle.loads(s.recv(500))
for i in data:
    print(f"got {i}" )
