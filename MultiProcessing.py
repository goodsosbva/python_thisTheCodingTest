import asyncio
import time


async def average(a):
    print("Avaerage start")
    k = 0
    for i in a:
        k += i
    #avg = k / (len(a) - 1)
    await asyncio.sleep(2.0)
    return k / (len(a))


async def printAvg(a):
    result = await average(a)
    print("%s" % (result))


loop = asyncio.get_event_loop()
loop.run_until_complete(printAvg([10, 50, 40, 100, 80]))
loop.close()
