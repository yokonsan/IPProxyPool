# coding=utf-8
from lxml import etree
from utils import parse_url

"http://www.ip181.com/"
"http://www.goubanjia.com/free/gngn/index.shtml"
"http://www.66ip.cn/areaindex_1/1.html"
"http://www.kuaidaili.com/free/inha/"
"http://www.xicidaili.com/"


class ProxyGetter(object):

    def ip181_proxy(self):
        url = 'http://www.ip181.com/'
        resp = parse_url(url)
        html = etree.HTML(resp)
        ips = html.xpath('//div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[1]/text()')[1:]
        ports = html.xpath('//div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr/td[2]/text()')[1:]
        for ip, port in zip(ips, ports):
            proxy = ip + ':' + port
            print(proxy)

    def ip66_proxy(self):
        for page in range(1, 9):
            url = 'http://www.66ip.cn/areaindex_{}/1.html'.format(page)
            resp = parse_url(url)
            html = etree.HTML(resp)
            ips = html.xpath('//*[@id="footer"]/div/table/tr/td[1]/text()')[1:]
            ports = html.xpath('//*[@id="footer"]/div/table/tr/td[2]/text()')[1:]
            for ip, port in zip(ips, ports):
                proxy = ip + ':' + port
                print(proxy)

    def xici_proxy(self):
        url = 'http://www.xicidaili.com/'
        resp = parse_url(url)
        html = etree.HTML(resp)
        ips = html.xpath('//*[@id="ip_list"]/tr[@class="odd"]/td[2]/text()')
        ports = html.xpath('//*[@id="ip_list"]/tr[@class="odd"]/td[3]/text()')
        for ip, port in zip(ips, ports):
            proxy = ip + ':' + port
            print(proxy)

    def kuai_proxy(self):
        for page in range(1, 4):
            url = 'http://www.kuaidaili.com/free/inha/{}/'.format(page)
            resp = parse_url(url)
            html = etree.HTML(resp)
            ips = html.xpath('//*[@id="list"]/table/tbody/tr/td[1]/text()')
            ports = html.xpath('//*[@id="list"]/table/tbody/tr/td[2]/text()')
            for ip, port in zip(ips, ports):
                proxy = ip + ':' + port
                print(proxy)


p = ProxyGetter()
p.kuai_proxy()
