import socket
import logging
import json
from classes import Student, Teacher, Guest

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
    logger.warning(f"{addr} someone connected from port {port}")

    if port % 3 == 0:
        data1 = Student('Nikita', 19, 'History')
    elif port % 3 == 1:
        data1 = Teacher('Igor', 57, "Calculus")
    else:
        data1 = Guest("Neptune", 10000, "Swimming")
    data = {
        "name": data1.name,
        "age": data1.age,
        "info": str(data1.inf())
        }
    client.send(json.dumps(data).encode())
    client.close()