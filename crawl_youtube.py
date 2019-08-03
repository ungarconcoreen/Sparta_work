# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import lxml
import json
import datetime

# URL을 읽어서 HTML를 받아오고,
data = requests.get('https://www.youtube.com/feed/trending')

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

video_info = {'title': '', 'video_link': '', 'img_link': '', 'play_time': '', 'hits': '', 'updated_time': '',
                  'description': '', 'reg_time': ''}

target_url = 'https://www.youtube.com/feed/trending'

response = requests.get(target_url)
soup = BeautifulSoup(response.text, "lxml")
lis = soup.find_all('li', {'class': 'expanded-shelf-content-item-wrapper'})

# li = lis[0]

for rank, li in enumerate(lis, 1):

    # exception
    title = li.find('a', {'title': True})['title']
    video_link = 'https://www.youtube.com' + li.find('a', {'href': True})['href']
    img_info = li.find('img', {'data-thumb': True})

    if img_info != None:
        img_link = img_info['data-thumb']
    else:
        img_link = li.find('img', {'src': True})['src']

    print(rank)
    print(video_link)
    print(img_link)
    print(title)
    print()

#
# video_set = soup.select('tr.list')
#
# video = video_set[0]
#
# for rank, video in enumerate(video_set, 1):
#
#     title = (video.select('td.info>a.title')[0].text.strip())
#     artist = (video.select('td.info>a.artist')[0].text.strip())
#     thumbnail = (video.select('img')[0].attrs['src'])


    # doc = {}
    # doc['rank'] = rank
    # doc['title'] = title
    # doc['artist'] = artist
    # doc['img'] = img
    #
    # db.youtube.insert_one(doc)



    # print(rank,title,artist)
    # print()

