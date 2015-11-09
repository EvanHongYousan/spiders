__author__ = 'yantianyu'

import re
import urllib
import urllib.request

from collections import deque

queue = deque()
visited = set()

url = 'https://s.2.taobao.com/list/list.htm?q=ps4&search_type=item&app=shopsearch/'

queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()

    visited |= {url}

    print('已经抓取：', str(cnt), '   正在抓取 <---', url)
    cnt += 1
    urlop = urllib.request.urlopen(url, timeout=2)
    if 'html' not in urlop.getheader('Content-Type'):
        continue

    try:
        data = urlop.read().decode('utf-8')
    except:
        continue

    linkre = re.compile('href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列 --->', x)
