"""
File: wangluoku3.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-05-26 16:35:44
Function:


"""
from urllib3 import *
from urllib.parse import urlencode
disable_warnings()
http1 = PoolManager()
url1 = 'http://www.baidu.com/s?' + urlencode({'wd': '极客起源'})
print(url1)
response = http1.request('GET', url1)
url2 = 'http://www.baidu.com/s'
response = http1.request('GET', url2, fields={'wd': '极客起源'})
data1 = response.data.decode('UTF-8')
print(data1)