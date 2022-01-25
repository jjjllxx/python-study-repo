"""
File: tupian.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-28 17:13:53
Function:


"""
import requests
path = 'D:/abc.mp4'
url = 'https://91mjw.com/vplay/MTA2Mi0xLTA=.html'
r = requests.get(url)
print(r.status_code)
with open(path, 'wb') as f:
    f.write(r.content)


