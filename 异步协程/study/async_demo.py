import asyncio
import time


async def func1():
    print("hello! async2!")
    await asyncio.sleep(2)
    print("hello! async1!")


async def func2():
    print("hello! async2!")
    await asyncio.sleep(5)
    print("hello! async2!")


async def func3():
    print("hello! async3!")
    await asyncio.sleep(3)
    print("hello! async3!")


async def main():
    tasks1 = [func1(), func2(), func3()]
    await asyncio.wait(tasks1)


if __name__ == '__main__':
    # tasks = [func1(), func2(), func3()]
    start = time.time()
    asyncio.run(main())
    end = time.time()
    time = end - start
    print(time)
