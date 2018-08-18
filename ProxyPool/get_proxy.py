# coding=utf-8
from lxml import etree
from ProxyPool.utils import parse_url


class ProxyMetaclass(type):
    """
    元类，在ProxyGetter类中加入
    __CrawlFunc__和__CrawlFuncCount__两个参数
    分别表示爬虫函数和爬虫函数的数量
    """
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k in attrs.keys():
            if k.startswith('proxy_'):
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class ProxyGetter(object, metaclass=ProxyMetaclass):
    """
    source:
        "http://www.66ip.cn/areaindex_1/1.html"
        "http://www.kuaidaili.com/free/inha/"
        "http://www.xicidaili.com/"
    """
    def get_raw_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('Getting', proxy, 'from', callback)
            proxies.append(proxy)
        return proxies

    def proxy_ip66(self):
        for page in range(1, 9):
            url = 'http://www.66ip.cn/areaindex_{}/1.html'.format(page)
            resp = parse_url(url)
            html = etree.HTML(resp)
            ips = html.xpath('//*[@id="footer"]/div/table/tr/td[1]/text()')[1:]
            ports = html.xpath('//*[@id="footer"]/div/table/tr/td[2]/text()')[1:]
            for ip, port in zip(ips, ports):
                proxy = ip + ':' + port
                yield proxy

    def proxy_xici(self):
        url = 'http://www.xicidaili.com/'
        resp = parse_url(url)
        html = etree.HTML(resp)
        ips = html.xpath('//*[@id="ip_list"]/tr/td[2]/text()')
        ports = html.xpath('//*[@id="ip_list"]/tr/td[3]/text()')
        for ip, port in zip(ips, ports):
            proxy = ip + ':' + port
            yield proxy

    def proxy_kuai(self):
        for page in range(1, 4):
            url = 'http://www.kuaidaili.com/free/inha/{}/'.format(page)
            resp = parse_url(url)
            try:
                html = etree.HTML(resp)
                ips = html.xpath('//*[@id="list"]/table/tbody/tr/td[1]/text()')
                ports = html.xpath('//*[@id="list"]/table/tbody/tr/td[2]/text()')
                for ip, port in zip(ips, ports):
                    proxy = ip + ':' + port
                    yield proxy
            except:
                pass


if __name__ == '__main__':
    pass
