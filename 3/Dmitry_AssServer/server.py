import asyncio
import pickle

from common import ADDR

class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = pickle.loads(data)
        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(message))
        self.transport.write(pickle.loads(message))

        print('Close the client socket')
        self.transport.close()


async def main():

    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        ADDR[0], ADDR[1])

    async with server:
        await server.serve_forever()


asyncio.run(main())