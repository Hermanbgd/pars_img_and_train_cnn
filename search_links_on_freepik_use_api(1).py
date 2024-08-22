import asyncio
from aiogram.client.session import aiohttp
import time


headers = {
    "authority": "ru.freepik.com",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36",
    "path": "/api/resources/12062880?locale=ru",
    "Cookie": 'filters-configs={"group":[{"name":"type","show":true},{"name":"license","show":true}],"show":true};'
              ' _gcl_au=1.1.663247000.1711369441; _ga=GA1.1.1051362909.1711369442; _tt_enable_cookie=1;'
              ' _ttp=wGcJChSMfE01aCUw-xmcnkhqneH; _pin_unauth=dWlkPU4yWmpPV05oTW1VdFpEUTVPUzAwT0dSbUxXSTBZalF0WmpWa09XSmlaV0prTTJNeg;'
              ' _cs_ex=1709818470; _cs_c=0; OptanonAlertBoxClosed=2024-03-25T12:24:06.383Z; g_state={"i_p":1711376722026,"i_l":1};'
              ' _fcid=FC.63cd9888-6e83-ac0f-d2f4-41a5101696ff; GR_LGURI=https://ru.freepik.com/popular; _ga_18B6QPTJPC=GS1.1.1714630787.5.1.1714630817.30.0.0; ads-tag=b;'
              ' _ga_QWX66025LC=GS1.1.1716366299.10.1.1716366914.60.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Wed+May+22+2024+12%3A35%3A14+GMT%2B0400+(%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&geolocation=RU%3BSAM&AwaitingReconsent=false',
    "Referer": "https://ru.freepik.com/search?ai=excluded&format=search&last_filter=page&last_value=1&page=1&query=%D1%81%D0%B2%D0%B5%D0%B6%D0%B5%D0%B5+%D1%8F%D0%B1%D0%BB%D0%BE%D0%BA%D0%BE&type=photo",
}

list_with_fruits = [['яблоко', 'apple'], ['банан', 'banana'], ['голубика', 'blueberry'], ['вишня', 'cherry'],
                    ['киви', 'kiwi'], ['лайм', 'lime'], ['апельсин', 'orange'], ['малина', 'raspberry'],
                    ['клубника', 'strawberry'], ['арбуз', 'watermelon']]


async def get_link(session, url):
    async with session.get(url) as response:
        data = await response.json()
        for item in data["items"]:
            if 'https://img.freepik.com/' in item["preview"]["url"]:
                list_with_links.append(item["preview"]["url"])


async def main(fruit):
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = []
        for p in range(1, 101):
            prem_url_json = f"https://ru.freepik.com/api/regular/search?filters[license]=premium&locale=ru&page={p}&term={fruit[0]}"
            task = asyncio.create_task(get_link(session, prem_url_json))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    for fruit in list_with_fruits[14:]:
        list_with_links = []
        start = time.time()
        asyncio.run(main(fruit))
        with open(f"fruits_links/links_{fruit[1]}", "w", encoding="utf-8") as file:
            for i in list_with_links:
                file.write(i + '\n')
        stop = time.time() - start
        print(f"{len(list_with_links)} ссылок на которых {fruit[0]} собрались за: {stop} секунд")
