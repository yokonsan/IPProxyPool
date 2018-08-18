# coding=utf-8
import requests
from requests.exceptions import ConnectionError


def parse_url(url, params=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'
    }
    if isinstance(params, dict):
        headers = dict(headers, **params)
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            return resp.text
        return None
    except ConnectionError:
        print('Error.')
    return None

