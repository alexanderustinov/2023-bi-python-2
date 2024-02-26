# server.py

import socket
import logging
import json

from classes import Laundry, Clothing

logger = logging.getLogger(__name__)
logging.basicConfig()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 3333))
s.listen(5)

s.setblocking(False)
s.settimeout(1)

while True:
    try:
        client_socket, addr = s.accept()
    except socket.timeout:
        continue
    client, (addr, port) = client_socket
    logger.warning(f"{addr} connected from port {port}")

    laundry = Laundry()
    socks = Clothing("Носки", "M")
    shirt = Clothing("Рубашка", "L")

    laundry.add_item(socks)
    laundry.add_item(shirt)

    data = {
        "items": [(item.name, 'чистое' if item.clean else 'грязное') for item in laundry.basket]
    }

    client.send(json.dumps(data).encode())
    client.close()

    
    



