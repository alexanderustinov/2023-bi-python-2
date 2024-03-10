import pickle
import asyncio
from random import randint

from common import ADDR
from classes import Guest, Student, Teacher


class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, on_con_lost):
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        transport.write(pickle.dumps(self.message))
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data))

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.on_con_lost.set_result(True)

rande = randint(0, 3)

async def main():

    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()
    if rande == 0:
        data1 = Student('Nikita', 19, 'History')
    elif rande == 1:
        data1 = Teacher('Igor', 57, "Calculus")
    else:
        data1 = Guest("Neptune", 10000, "Swimming")
    data = pickle.dumps(data1)

    transport, protocol = await loop.create_connection(
        lambda: EchoClientProtocol(data1, on_con_lost), ADDR[0], ADDR[1])

    try:
        await on_con_lost
    finally:
        transport.close()

asyncio.run(main())
