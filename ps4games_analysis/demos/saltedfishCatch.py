__author__ = 'yantianyu'

import requests
from bs4 import BeautifulSoup
from collections import deque
import time

queue = deque()
visited = set()

url = 'https://s.2.taobao.com/list/list.htm?q=%D1%AA%D4%B4%D7%E7%D6%E4&search_type=item&app=shopsearch'
# url='https://www.baidu.com'
# url = 'http://www.taobao.com/'

queue.append(url)
cnt = 0

# response = requests.get(url)
# soup = BeautifulSoup(response.text)
# hrefs = soup.find(id='J_Pages').find_all('a')
# for items in hrefs:
# print('https:'+items['href'])

while queue:
    url = queue.popleft()

    visited.add(url)
    print('已经抓取:', str(cnt), '正在抓取 <---', url)
    print('当前len(visited)：', len(visited))
    print('当前len(queue):', len(queue))
    cnt += 1

    time.sleep(2)
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    hrefs = soup.find(id='J_Pages').find_all('a')
    tempurls = []
    for href in hrefs:
        tempurls.append('https:'+href['href'])
    for item in tempurls:
        if item not in visited and item not in queue:
            queue.append(item)
            print('加入队列--->', item)
            with open('queue.txt', 'w') as f:
                temp = ''
                for queI in queue:
                    temp += queI + '\n'
                f.write(str(temp))
                f.close()
            with open('visited.txt', 'w') as f:
                temp = ''
                for visiI in visited:
                    temp += visiI + '\n'
                f.write(str(temp))
                f.close()

