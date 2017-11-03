# IP代理池

### 项目介绍

本项目通过爬虫抓取互联网上免费代理网站的IP，并且进行异步检测是否可用，如果可用就放入数据库。定时对数据库中的代理进行维护，然后通过web api的形式供外部使用。

### 代理池设计

* Getter：代理获取接口，项目只放入4个免费代理网站，支持自由添加；

* Mongodb：Mongodb数据库存放抓取并且有效的代理，如需扩展，结合对应数据库api；

* Schedule：计划任务，爬虫的启动，添加代理，测试代理，定时检测代理；

* Api：代理池的外部接口，利用`flask`简单实现。


### 安装

Git下载代码：

```
git clone git@github.com:Blackyukun/IPProxyPool.git
```

直接下载：[下载](https://github.com/Blackyukun/IPProxyPool/archive/master.zip)

依赖安装：

```
pip install -r requirements.txt
```


### 使用

```
>>> python run.py
```

启动成功，打开浏览器，127.0.0.1:5000查看。

爬虫中获取代理：

```Python
import requests

def get_proxy():
    resp = requests.get('http://127.0.0.1:5000/get')
    proxy = resp.text
    ip = 'http://' + proxy
    return ip
```

### Enjoy it
