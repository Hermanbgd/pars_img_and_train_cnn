import os
import time
import aiofiles
import aiohttp
import asyncio

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36"
}
list_with_fruits = [['яблоко', 'apple'], ['банан', 'banana'], ['голубика', 'blueberry'], ['вишня', 'cherry'],
                    ['киви', 'kiwi'], ['лайм', 'lime'], ['апельсин', 'orange'], ['малина', 'raspberry'],
                    ['клубника', 'strawberry'], ['арбуз', 'watermelon']]


async def write_file(session, url, name_img, fruit):
    async with aiofiles.open(f'fruits_images/{fruit[1]}_images/{name_img}.jpg', mode='wb') as f:
        async with session.get(url) as response:
            async for x in response.content.iter_chunked(1024):
                await f.write(x)
        # print(f'Изображение сохранено {name_img}')


async def main(fruit):
    with open(f"fruits_links/links_{fruit[1]}", "r") as f:
        test_list = f.read().splitlines()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for e, link in enumerate(test_list):
            task = asyncio.create_task(write_file(session, link, f"{fruit[1]}.{e+1}", fruit))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    for fruit in list_with_fruits:
        start = time.perf_counter()
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main(fruit))
        print(f'{fruit[0]} {len(os.listdir(f"fruits_images/{fruit[1]}_images/"))} изображений сохранено за {round(time.perf_counter() - start, 3)} сек')



