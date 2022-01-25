"""
File: biaotou.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-05-26 16:17:01
Function:


"""
from urllib import request, parse
url1 = 'http://httpin.org/post'
headers1 = {'User=Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Host': 'httpbin.org',
            'who': 'Python Scrapy'}
dict1 = {'name': 'Bill', 'age': 30}
data1 = bytes(parse.urlencode(dict1), encoding='utf-8')
req = request.Request(url=url1, data=data1, headers=headers1)
response = request.urlopen(req)
print(response.read().decode('utf-8'))