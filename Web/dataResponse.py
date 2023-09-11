"""
File: shujuxiangying.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-05-26 20:25:19
Function:


"""
import requests
kv = {'User=Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                    ' (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
r = requests.get('http://www.jianshu.com', headers=kv)
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)
if not r.status_code == requests.codes.ok:
    print('failed')
else:
    print('ok')
