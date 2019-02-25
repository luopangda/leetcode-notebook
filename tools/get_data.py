import urllib.request
import json


def get_data_by_link(url):
    """
    :param url: 爬取数据的连接
    :return: 返回最原始的数据
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url, headers=headers)
    web_url = urllib.request.urlopen(req)
    raw_data = json.loads(web_url.read())
    return raw_data