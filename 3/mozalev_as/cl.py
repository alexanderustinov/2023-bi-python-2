import asyncio
import pickle
class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, on_con_lost):
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print(f'Клиент сказал: {self.message}')

    def data_received(self, data):
        #print(f'Сервер ответил: {data.decode()}')
        customer = pickle.loads(data)
        customer.view_cart()

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.on_con_lost.set_result(True)


async def main():
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()
    message = 'Покажи шо умеешь'

    transport, protocol = await loop.create_connection(
        lambda: EchoClientProtocol(message, on_con_lost),
        '127.0.0.1', 3333)

    try:
        await on_con_lost
    finally:
        transport.close()


asyncio.run(main())