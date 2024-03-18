import asyncio
from common import ADDR
from random import randint
import pickle

from classes import Stars, Planets

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

rand = randint(0, 2)

async def main():
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()
    if rand == 0:
        datan = Stars(6.9551*(10**8), 1.9885*(10**30), 1.496*(10**11))
    else:
        datan = Planets(6378.1*(10**3), 465.1, 5.9726*(10**24), 12742)
    data = pickle.dumps(datan)

    transport, protocol = await loop.create_connection(
        lambda: EchoClientProtocol(datan, on_con_lost),
        ADDR[0], ADDR[1])

    try:
        await on_con_lost
    finally:
        transport.close()


asyncio.run(main())
