from asyncio import run as async_run
from autoproxy.__utils import proxyScraper
from autoproxy.sources import sources
from random import choice

class autoProxy:
    isInited: bool = False
    scrap_proxies: dict = {
        'http': [],
        'socks4': [],
        'socks5': []
    }
    
    def __init__(
            self, sources: dict =sources, 
            logging: bool =False, 
        ):
        self.proxy_sources = sources
        self.logging = logging
        
    def init(self):
        autoProxy.isInited = False
        autoProxy.scrap_proxies = {'http': [], 'socks4': [], 'socks5': []}
        ap = proxyScraper(
            logging=self.logging, 
            sources=self.proxy_sources, 
        )
        async_run(ap.start_scrapping())
        autoProxy.scrap_proxies =  ap.scrap_proxies
        autoProxy.isInited = True


class Auto:
    def __init__(self, proxy_type: str):
        self.proxy_type = proxy_type
        self.proxy_types = ['http', 'socks4', 'socks5']
        assert proxy_type in self.proxy_types + ['all'], 'ProxyTypes are: http, socks4, socks5'
        assert autoProxy.isInited == True, 'AutoProxy is not Inited'

    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            if self.proxy_type == 'all':
                proxy_type = choice(self.proxy_types)
                proxy = choice(autoProxy.scrap_proxies[proxy_type])
            else:
                proxy_type = self.proxy_type
                proxy = choice(autoProxy.scrap_proxies[proxy_type])

            proxies = {
                'http': f'{proxy_type}://{proxy}',
                'https': f'{proxy_type}://{proxy}'
            }
            
            return func(proxies=proxies, *args, **kwargs)
        return wrapped_func