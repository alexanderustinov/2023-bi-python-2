from common import AD,DR
import asyncio
import pickle
class Fr:
    def __init__(self, message):
        self.message = message
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

async def main():
    loop = asyncio.get_event_loop()
    on_con_lost = loop.create_future()
    data1 = Fr('Мандаринчики')
    data = pickle.dumps(data1)

    transport, protocol = await loop.create_connection(
        lambda: EchoClientProtocol(data1, on_con_lost), AD, DR)

    try:
        await on_con_lost
    finally:
        transport.close()

asyncio.run(main())
