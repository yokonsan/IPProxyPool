# Mongodb数据库
NAME = 'proxy'
HOST = 'localhost'
PORT = 27017

# 供测试的url
TEST_URL = 'http://www.baidu.com'

# Pool 的低阈值和高阈值
POOL_LOWER_THRESHOLD = 10
POOL_UPPER_THRESHOLD = 40

# 两个调度进程的周期
VALID_CHECK_CYCLE = 600
POOL_LEN_CHECK_CYCLE = 20

# 获得代理测试时间界限
GET_PROXY_TIMEOUT = 9
