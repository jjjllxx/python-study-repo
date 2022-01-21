"""
File: zhongwen.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-02-01 17:10:42
Function:


"""
import jieba

text = '我爱北京天安门'
a = "".join(list(jieba.cut(text)))
print(a)
