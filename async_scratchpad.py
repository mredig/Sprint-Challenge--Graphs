import asyncio


async def nested(values):
    # await asyncio.sleep(1)
    values.append(42)


async def nested2(values):
    values.append(69)

def other(values):
    values.append(100)

async def conReturn():
    return 42

async def conReturn2():
    return 69

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    values = []
    # task = asyncio.create_task(nested(values))
    # task = asyncio.create_task(nested2(values))
    stressList = []
    # for test in range(999999):
    #     stressList.append(nested(values))
    value = await asyncio.gather(
        conReturn(),
        conReturn2()
    )

    print("value: ", value)

    # task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    # return 5


# main()

def altMain():
    print(asyncio.run(main()))

altMain()