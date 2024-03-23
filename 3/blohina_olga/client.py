import asyncio
import pickle
from common import ADDR

async def Client():
    reader, writer = await asyncio.open_connection(ADDR[0], ADDR[1])
    answer = await reader.read(1024)
    data = pickle.loads(answer)
    for i in data:
        print(f'Received {i}' )
    writer.close()

if __name__ == '__main__':
    asyncio.run(Client())
