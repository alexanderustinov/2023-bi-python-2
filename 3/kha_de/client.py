import asyncio

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
        self.transport.sendto(self.message.encode())

    def datagram_received(self, data, addr):
        print("Received:", data.decode())

        print("I'm closing?")
        self.transport.close()

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print("Bye-Bye :(")
        self.on_con_lost.set_result(True)


async def main():
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        aaaa = ('127.0.0.1', 3333))


async def main():
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()
    message = bird.swim()

    transport, protocol = await loop.create_datagram_endpoint(
        lambda: EchoClientProtocol(message, on_con_lost),
        remote_addr=AAA)

    try:
        await on_con_lost
    finally:
        transport.close()

asyncio.run(main())