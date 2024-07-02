from strategy import Strategy

import asyncio


async def main():
    strategy = Strategy()
    await strategy.connect_streams()
    while True:
        await strategy.on_tick()


if __name__ == '__main__':
    asyncio.run(main())


