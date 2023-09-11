"""
File: xiaoshuo.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-03-23 09:54:59
Function:

get a novel named Legend of Dragon King, can set the number of chapter manually,
saved in folder named with Legend of Dragon King in D-disk

爬取小说龙王传说，可以选择爬取章节数，保存在D盘文件夹‘龙王传说’

"""
import requests
import re
import time
import os


def getHTMLText(url):  # get the page with chapter url 获取包含章节url的页面
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def getChapterUrls(html):  # get url of each chapter 获取每一章节的url
    chapter_urls_new = []
    chapter_urls = re.findall(r'<dd><a href="(.*?)">.*?</a></dd>', html)
    for i in chapter_urls:
        chapter_urls_new.append('http://www.89wxw.cn' + i)
    return chapter_urls_new


def getChapterName(html):  # get name of each chapter to save files 获取章节的名称，用以保存文件
    chapter_name = re.findall(r'<dd><a href=".*?">(.*?)</a></dd>', html)
    return chapter_name


def getWords(chapter_urls_new, chapter_name, num=1):  # create a folder and txt file for each chapter 创建文件夹，以及包含每一章节的txt
    error_chapter = []
    if num > len(chapter_name):
        num = len(chapter_name)

    dirs = 'D:/Legend of Dragon King'  # 龙王传说
    if not os.path.exists(dirs):
        os.makedirs(dirs)

    for i in range(num):
        time.sleep(1)
        try:
            html = getHTMLText(chapter_urls_new[i])
            words = re.findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />', html)
            for word in words:
                path = 'D:/Legend of Dragon King/' + '0'*(4-len(str(i)))+str(i)+chapter_name[i] + '.txt'
                with open(path, 'a', encoding='utf-8') as file_object:
                    file_object.write(word + '\n')
        except:
            error_chapter.append(i)
            continue
    return error_chapter


def reportError(error_chapter):  # error feedback 错误反馈
    print('download finished')  # 下载完毕
    for i in error_chapter:
        print(f'chapter no.{i}', end=' ')  #
    print('error happens')  # 出现错误


def main():  # 主程序
    while True:
        try:
            num = int(input('enter number of chapters to download: '))  # 下载章节数
            break
        except:
            print('illegal number, enter again')  # 输入非法数字请重新输入
            continue
    print('downloading...')  # 开始下载
    url = 'http://www.89wxw.cn/0/9/'
    html = getHTMLText(url)
    chapter_urls_new = getChapterUrls(html)
    chapter_name = getChapterName(html)
    error_chapter = getWords(chapter_urls_new, chapter_name, num)
    reportError(error_chapter)


if __name__ == '__main__':
    main()
