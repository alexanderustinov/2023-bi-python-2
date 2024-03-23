import asyncio
from classes_5 import Customer, Product
import random
import pickle

def try_use_classes():
    product1 = Product("Футболка", 500)
    product2 = Product("Джинсы", 1000)
            
    quantity1 = random.randint(1, 5)
    quantity2 = random.randint(1, 5)

    customer = Customer("Иван")
    customer.add_to_cart(product1, quantity1)
    customer.add_to_cart(product2, quantity2)
    return customer

class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Клиент сказал: {}'.format(message))
        
        customer = try_use_classes()
        answer = pickle.dumps(customer)
        #print('Сервер ответил: {}'.format(answer))
        print('Сервер ответил')
        self.transport.write(answer)

        print('Close the client socket')
        self.transport.close()


async def main():
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        '127.0.0.1', 3333)

    async with server:
        await server.serve_forever()


asyncio.run(main())