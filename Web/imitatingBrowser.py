"""
File: moniliulanqi.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-28 16:55:43
Function:


"""
import requests

kv = {'user-agent': 'Mozilla/5.0'}
url = 'https://www.amazon.cn/dp/B00S4OK1ZS/ref=sr_1_1?__mk_zh_CN=亚马逊网站&keywords=三体&qid=1582880330&sr=8-1'
try:
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)

except:
    print('abnormal status')  # 状态异常

