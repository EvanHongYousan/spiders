__author__ = 'yantianyu'
__version__ = 1.1

import requests
import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup
from collections import deque
import time
import csv

queue = deque()
visited = set()

print('author: EvanHongYousan')
print('Email: 1370204201@qq.com')
print('github: https://github.com/EvanHongYousan')
print('工具用于抓取淘宝闲鱼2手市场上的物品数据，并生成 [价格|标题|网址] 格式的excel文件')
searchQuery = input('输入要搜索物品的关键词：')

url = 'https://s.2.taobao.com/list/list.htm?q=' + quote(searchQuery, '', 'gb2312') + '&search_type=item&app=shopsearch'
# url='https://www.baidu.com'
# url = 'http://www.taobao.com/'

queue.append(url)
cnt = 0
blbnObjs = []

# response = requests.get(url)
# soup = BeautifulSoup(response.text)
# hrefs = soup.find(id='J_Pages').find_all('a')
# for items in hrefs:
# print('https:'+items['href'])

def getUrls(data):
    hrefs = data.find(id='J_Pages').find_all('a')
    tempurls = []
    for href in hrefs:
        tempurls.append('https:' + href['href'])
    return tempurls


def getBlbnObj(data):
    dataContainers = []
    data = data.find(id='J_ItemListsContainer')
    items = data.find(attrs={'class': 'item-lists'}).findAll(attrs={'class': 'item-idle'})
    for item in items:
        title = item.find('div', {'class': 'item-info'}).find('h4', {'class': 'item-title'}).find('a').contents[0]
        price = item.find('div', {'class': 'item-info'}).find('div', {'class': 'item-price'}).find('em').contents[0]
        url = 'http:' + item.find('div', {'class': 'item-info'}).find('h4', {'class': 'item-title'}).find('a')['href']
        location = \
            item.find('div', {'class': 'seller-info-wrapper'}).find('div', {'class': 'seller-info'}).find('div', {
                'class': 'seller-location'}).contents[0]
        dataContainers.append((price, location, title, url))
    return dataContainers


while queue:
    url = queue.popleft()

    visited.add(url)
    print('已经抓取:', str(cnt), '正在抓取 <---', url)
    print('当前len(visited)：', len(visited))
    print('当前len(queue):', len(queue))
    cnt += 1

    time.sleep(2)
    # response = requests.get(url)
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read())

    blbnObjs.extend(getBlbnObj(soup))

    tempurls = getUrls(soup)
    for item in tempurls:
        if item not in visited and item not in queue:
            queue.append(item)
            print('加入队列--->', item)

with open('visited.txt', 'w') as f:
    temp = ''
    for visiI in visited:
        temp += visiI + '\n'
    f.write(str(temp))
    f.close()

print(blbnObjs)

with open('【关键词：' + searchQuery + '】淘宝闲鱼抓取结果.csv', 'w', newline='') as csvF:
    writer = csv.writer(csvF)
    writer.writerow([u'价格', u'所在地', u'标题', u'网址'])
    writer.writerows(sorted(blbnObjs, key=lambda item: float(item[0])))
    csvF.close()
