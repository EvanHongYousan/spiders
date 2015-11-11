__author__ = 'yantianyu'

import requests
from bs4 import BeautifulSoup

url = 'https://s.2.taobao.com/list/list.htm?q=%D1%AA%D4%B4%D7%E7%D6%E4&search_type=item&app=shopsearch'
# url='https://www.baidu.com'
url = 'http://www.douban.com/'
response = requests.get(url)
print(response.text)

