import asyncio


async def loop_print_100():
    for i in range(10):
        print(i)
        await asyncio.sleep(2)


async def print_test():
    for _ in range(20):
        print("test")
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(loop_print_100())
    task2 = asyncio.create_task(print_test())
    await task1
    await task2


if __name__ == "__main__":
    asyncio.run(main())
