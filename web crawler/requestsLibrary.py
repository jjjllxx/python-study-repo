"""
File: requestsku.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-28 15:37:07
Function:


"""
import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return print(r.text)
    except:
        return print('abnormal status')  # 状态异常


if __name__ == '__main__':
    url = 'https://item.jd.com/31648939594.html'
    getHTMLText(url)
