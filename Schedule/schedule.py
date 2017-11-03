import time
from multiprocessing import Process

from ProxyPool.db import MongodbClient
from .tester import ProxyTester
from .adder import PoolAdder
from config import *


class Schedule(object):

    @staticmethod
    def valid_proxy(cycle=VALID_CHECK_CYCLE):
        """
        从数据库中拿到一半代理进行检查
        """
        conn = MongodbClient()
        tester = ProxyTester()
        while True:
            print('Refreshing ip...')
            count = int(0.5 * conn.get_nums)
            if count == 0:
                print('Waiting for adding...')
                time.sleep(cycle)
                continue
            raw_proxies = conn.get(count)
            tester.set_raw_proxies(raw_proxies)
            tester.test()
            time.sleep(cycle)

    @staticmethod
    def check_pool(lower_threshold=POOL_LOWER_THRESHOLD,
                upper_threshold=POOL_UPPER_THRESHOLD,
                cycle=POOL_LEN_CHECK_CYCLE):
        """
        如果代理数量少于最低阈值，添加代理
        """
        conn = MongodbClient()
        adder = PoolAdder(upper_threshold)
        while True:
            if conn.get_nums < lower_threshold:
                adder.add_to_pool()
            time.sleep(cycle)

    def run(self):
        print('Ip Processing running...')
        valid_process = Process(target=Schedule.valid_proxy)
        check_process = Process(target=Schedule.check_pool)
        valid_process.start()
        check_process.start()
