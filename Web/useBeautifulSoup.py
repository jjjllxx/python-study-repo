"""
File: meiweitang.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-03-04 20:06:28
Function:


"""
import requests
from bs4 import BeautifulSoup

r = requests.get('https://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

print(soup.a.prettify())
