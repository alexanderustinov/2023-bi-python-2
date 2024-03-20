import asyncio
import pickle

from common import AAA
from penguin import *

class EchoClientProtocol:
    def __init__(self, message, on_con_lost):
        self.message = message
        self.on_con_lost = on_con_lost
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        print(self.message)
        self.transport.sendto(pickle.dumps(self.message))

    def datagram_received(self, data, addr):
        print("Received: {!r}".format(data))

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print("Bye-Bye :(")
        self.on_con_lost.set_result(True)

async def main():
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()
    message = 'Let`s go!'

    r = randint(0, 20)
    if r % 2 == 0:
        bird = Penguin('Emperor Penguin', '130', '25', '35', '40')
    else:
        bird = Penguin('Rockhopper Penguin', '60', '25', '2', '3')

    data = pickle.dumps(bird)


    transport, protocol = await loop.create_datagram_endpoint(
        lambda: EchoClientProtocol(bird, on_con_lost),
        remote_addr=AAA)

    try:
        await on_con_lost
    finally:
        transport.close()

asyncio.run(main())


