import asyncio
import pickle
from МузыкаКлассы2 import *
from common import ADDR
class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, on_con_lost):
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        transport.write(pickle.dumps(self.message))
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode))

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.on_con_lost.set_result(True)

async def main():
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()

    data0 = [Genre, Ganre2, Ganre3]
    message = pickle.dumps(data0)

    transport, protocol = await loop.create_connection(
        lambda: EchoClientProtocol(message, on_con_lost),
                ADDR[0],ADDR[1])
    try:
        await on_con_lost
    finally:
        transport.close()
asyncio.run(main())

