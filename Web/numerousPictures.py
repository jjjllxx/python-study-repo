"""
File: daliang.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-29 15:17:55
Function:

use requests and re library to get a lot of pictures

"""
import requests
import re
import time

"""request page/请求网页"""

kv = {'user-agent': 'Mozilla/5.0'}
url = 'http://jandan.net/ooxx/MjAyMDAyMjktMjAz#comments'

response = requests.get(url, headers=kv)
# print(response.status_code)
html = response.text

"""parse page/解析网页"""
urls = re.findall('</a></span><p><a href="(.*?)" target="_blank" class=".*?" referrerPolicy=".*?">', html)
urls_after = []
for i in urls:
    urls_after.append('https:' + i)
print(urls_after)

path = 'D:/pictures'
for i in urls_after:
    time.sleep(1)
    r = requests.get(i, headers=kv)
    with open(path + '/' + i.split('/')[-1], 'wb') as f:
        f.write(r.content)
