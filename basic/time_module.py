"""
File: shijian.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-03-24 17:32:07
Function:


"""

import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
print(yesterday)
hours = today - datetime.timedelta(hours=1)
print(hours)