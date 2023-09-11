"""
File: xinxitiqu.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-03-05 19:49:27
Function:


"""
import re
import requests
from bs4 import BeautifulSoup

r = requests.get('https://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

# for link in soup.find_all('a'):
#     print(link.get('href'))

# for tag in soup.find_all(re.compile('b')):
#     print(tag.name, end=' ')

print(soup.find_all(string=re.compile('Python')))