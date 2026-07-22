import asyncio


async def work(name, delay):
    print(f"{name} started")

    await asyncio.sleep(delay)

    print(f"{name} middle")

    await asyncio.sleep(1)

    print(f"{name} finished")

    return name


async def main():
    print("MAIN started")

    task1 = asyncio.create_task(work("A", 2))

    print("A task created")

    result_b = await work("B", 1)

    print("Got B:", result_b)

    task2 = asyncio.create_task(work("C", 1))

    print("C task created")

    result_a = await task1

    print("Got A:", result_a)

    result_c = await task2

    print("Got C:", result_c)

    print("MAIN finished")


asyncio.run(main())