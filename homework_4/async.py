import asyncio
import aiohttp
import time
from urls import urls


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            filename = url.replace("https://", "").split("/")[-1]
        with open(f"homework_4/img/async-{filename}", "wb") as f:
            f.write(response)
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
        await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == "__main__":
    asyncio.run(main())
