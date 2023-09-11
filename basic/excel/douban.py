"""
File: douban.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-05-24 15:25:40
Function:


"""
import requests
import re
import time
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def getName(html):
    name_new = []
    name = re.findall(r'<span class="title">(.*?)</span>', html)
    for i in name:
        if i[0] == '&':
            continue
        else:
            name_new.append(i)
    return name_new


def getDescription(html):
    des = []
    des_new = []
    soup = BeautifulSoup(html, 'html.parser')
    p_tags = soup.find_all('p', class_='')
    for i in p_tags:
        des.append(i.text.split('\n')[1].strip()+i.text.split('\n')[2].strip())
    for i in des:
        des_new.append(i.replace('\xa0', ''))
    return des_new


def combineNameDes(name, des):
    after_sentence = []
    for i in range(len(name)):
        after_sentence.append(name[i]+' '+des[i])
    return after_sentence


def main():
    sentence_all = []
    for i in range(10):
        url = 'https://movie.douban.com/top250?start='+str(25*i)+'&filter='
        html = getHTMLText(url)
        names = getName(html)
        miaoshu = getDescription(html)
        sentence = combineNameDes(names, miaoshu)
        sentence_all.extend(sentence)
        time.sleep(1)
    path = 'D:/douban.txt'
    for j in sentence_all:
        with open(path, 'a', encoding='utf-8') as file_object:
            file_object.write(j + '\n'+'\n')


if __name__ == '__main__':
    main()
