import asyncio
import aiohttp

from ProxyPool.db import MongodbClient
from config import TEST_URL


class ProxyTester(object):
    test_url = TEST_URL

    def __init__(self):
        self._raw_proxies = None

    def set_raw_proxies(self, proxies):
        self._raw_proxies = proxies
        self._conn = MongodbClient()

    async def test_single_proxy(self, proxy):
        """
        测试一个代理，如果有效，将他放入数据库
        """
        try:
            async with aiohttp.ClientSession() as session:
                try:
                    if isinstance(proxy, bytes):
                        proxy = proxy.decode('utf-8')
                    real_proxy = 'http://' + proxy
                    print('Testing', proxy)
                    async with session.get(self.test_url, proxy=real_proxy, timeout=10) as response:
                        if response.status == 200:
                            self._conn.put(proxy)
                            print('Valid proxy', proxy)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

    def test(self):
        """
        异步测试所有代理
        """
        print('Tester is working...')
        try:
            loop = asyncio.get_event_loop()
            tasks = [self.test_single_proxy(proxy) for proxy in self._raw_proxies]
            loop.run_until_complete(asyncio.wait(tasks))
        except ValueError:
            print('Async Error')
