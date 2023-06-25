import aiohttp, asyncio
from re import compile

class proxyScraper:
    __REGEX = compile(
        r"(?:^|\D)?(("+ r"(?:[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
        + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
        + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
        + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
        + r"):" + (r"(?:\d|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}"
        + r"|65[0-4]\d{2}|655[0-2]\d|6553[0-5])")
        + r")(?:\D|$)"
    )

    def __init__(self, sources, logging=False):
        self.sources = sources
        self.logging: bool = logging
        self.TIMEOUT: int = 15
        self.USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        self.scrap_proxies: dict = {
            'http': [],
            'socks4': [],
            'socks5': []
        }

    async def __scrap(self, url: str, proxy_type: str):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    url, headers={'user-agent': self.USER_AGENT}, 
                    timeout=aiohttp.ClientTimeout(total=self.TIMEOUT)
                ) as response:
                    html = await response.text()
                    if tuple(proxyScraper.__REGEX.finditer(html)):
                        for proxy in tuple(proxyScraper.__REGEX.finditer(html)):
                            self.scrap_proxies[proxy_type].append(proxy.group(1))
                    else: (
                            self.logging and 
                            print(f" [AutoProxy] Cant Find Proxies At: {url}")
                        )
        except Exception as e: (
                self.logging and 
                print(f" [AutoProxy]: Error While Scrapping {url} {e}")
            )

    async def start_scrapping(self):
        (
            self.logging and 
            print(f" [AutoProxy]: Start Scrapping")
        )
        for source in self.sources:
            await asyncio.gather(
                    *[ asyncio.create_task(
                    self.__scrap(url, proxy_type=source)) 
                    for url in self.sources[source] ]
                )



