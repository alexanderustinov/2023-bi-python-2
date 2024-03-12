import asyncio
import logging
import pickle

from common import AD,DR

logger = logging.getLogger(__name__)
logging.basicConfig()

class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = pickle.loads(data)
        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(message.inf()))
        self.transport.write(pickle.loads(data).inf().encode())

        print('Close the client socket')
        self.transport.close()



async def main():

    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        AD,DR)

    async with server:
        await server.serve_forever()


asyncio.run(main())
