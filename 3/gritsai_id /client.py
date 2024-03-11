import asyncio
import pickle

from common import ADDR

async def main():
    reader, writer = await asyncio.open_connection(*ADDR)

    data = await reader.read(4096)
    laundry = pickle.loads(data)
    laundry.show_items()
    laundry.wash()
    laundry.show_items()

    writer.close()
    await writer.wait_closed()

asyncio.run(main())
