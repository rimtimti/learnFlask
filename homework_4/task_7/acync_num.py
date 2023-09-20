import asyncio
import time
from treads_num import LENGTH, MIN, MAX, CUT, get_random_array, cut_array


async def sum_number(array):
    global summa
    summa += sum(array)
    print(f"Sum numbers = {summa} counted in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for i in cut_array(array, CUT):
        task = asyncio.create_task(sum_number(i))
        tasks.append(task)
        await asyncio.gather(*tasks)


summa = 0

array = get_random_array(LENGTH, MIN, MAX)
start_time = time.time()

if __name__ == "__main__":
    asyncio.run(main())
