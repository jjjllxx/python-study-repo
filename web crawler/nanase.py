"""
File: nanase.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-03-07 20:55:19
Function:
to get a large amount of pictures from Baidu Tieba, turning page automatically, saved in a folder named nanase in
D-disk, for each page, saved in subfolder respectively
爬取百度贴吧一个帖子里的图片，自带翻页，保存在D盘nanase文件夹中，每页的图片也分别被保存在一个子文件夹中

"""
import requests
import re
import time
import os


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def getPicture(html):
    pictures_url = re.findall('<img class=".*?" src="(.*?)" size=".*?" changedsize=".*?" width=".*?" height=".*?" size=".*?"><br>', html)
    return pictures_url


def savePictures(picture_url, url):
    path = 'D:/nanase/'+url.split('?')[-1]
    if not os.path.exists(path):
        os.makedirs(path)
    for urls in picture_url:
        time.sleep(1)
        r = requests.get(urls)
        with open(path + '/' + urls.split('/')[-1], 'wb') as f:
            f.write(r.content)


def main():
    dirs = 'D:/nanase'
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    num = int(input('Please enter number of pages'))  # 输入下载页数
    print('start downloading')  # 开始下载
    for i in range(1, num+1):
        try:
            url = 'https://tieba.baidu.com/p/6222630845?pn='+str(i)
            html = getHTMLText(url)
            pictures_url = getPicture(html)
            savePictures(pictures_url, url)
        except:
            print(f'Error happens at page{i}')  # 下载某页时出现错误
            continue
    print('Download finished')  # 下载完毕


if __name__ == '__main__':
    main()

