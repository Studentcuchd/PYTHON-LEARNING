import asyncio

async def work(name, t):
    print(f"{name} Start")
    await asyncio.sleep(t)
    print(f"{name} End")
    return name

async def main():
    t = asyncio.create_task(work("A", 2))

    await asyncio.sleep(1)

    print(await t)

    print(await t)

asyncio.run(main())