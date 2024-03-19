import asyncio
import pickle

from common import AAA
from penguin import *

class EchoServerProtocol:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = pickle.loads(data)
        print('Received %r from %s' % (message, addr))
        print('Send %r to %s' % (message.swim(), addr))
        self.transport.sendto(pickle.loads(data).swim().encode(), addr)

        print("I'm closing?")
        self.transport.close()

async def main():
    print("Hiiiii! I'm starting.")
    loop = asyncio.get_running_loop()

    transport, protocol = await loop.create_datagram_endpoint(
        lambda: EchoServerProtocol(),
        local_addr = AAA)

    try:
        await asyncio.sleep(60)
    finally:
        transport.close()


asyncio.run(main())