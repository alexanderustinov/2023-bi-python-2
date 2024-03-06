# client.py

import socket
import json

from classes import Item, Laundry, Clothing

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 3333))
data = json.loads(s.recv(500).decode())
print("Список белья в прачечной:")
for item_name, clean_status in data['items']:
    print(f"{item_name} ({clean_status})")
s.close()
