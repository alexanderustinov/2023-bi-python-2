import socket
import pickle

from common import ADDR
from classes import Item, Laundry, Clothing

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

data = s.recv(4096)
laundry = pickle.loads(data)
laundry.show_items()
laundry.wash()
laundry.show_items()

s.close()
