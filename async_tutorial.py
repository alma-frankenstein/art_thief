import asyncio
import random

#--------------countsync---------------------------

# async def count():  # coroutine
#     print("one")
#     await asyncio.sleep(1)  # do the next thing while we wait for this. Can only use 'await' in the body of coroutines
#                             # awaited object has to be another coroutine
#     print("two")
    
# async def main():
#     await asyncio.gather(count(), count(), count())
    
# if __name__=="__main__":
#     import time
#     s = time.perf_counter()
#     asyncio.run(main())
#     elapsed = time.perf_counter() - s
#     print(f"{__file__} ran in {elapsed:0.2f} seconds")

#--------------------rand----------------------------------

colors = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

async def makerandom(idx: int, threshold: int = 6) -> int:  # function annotation: expected argument and return values
    print(colors[idx + 1] + f"initiated makerandom {idx}")
    i = random.randint(1, 10)
    while i <= threshold:
        print(colors[idx + 1] + f"makerandom {idx} == {i} too low, retrying")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(colors[idx + 1] + f"--> finished makerandom {idx} == {i}" + colors[0])
    return i

async def main():
    res = await asyncio.gather(*(makerandom(i, 10-i-1) for i in range(3)))
    return res

if __name__=="__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")