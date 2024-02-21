import socket
import logging
import json
import random
import datetime

from common import ADDR

logger = logging.getLogger(__name__)
logging.basicConfig()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c = s.bind(ADDR)
s.listen(5)

s.setblocking(False)
s.settimeout(1)

while True:
    try:
        client_socket = s.accept()
    except TimeoutError:
        continue
    client, (addr, port) = client_socket
    logger.warning(f"{addr} connected from port {port}")

    data = {
        "time": datetime.datetime.now().isoformat(),
        "number": random.random()
        }

    client.send(json.dumps(data).encode())
    # b''.decode()
    # "".encode()
    client.close()
    
    



