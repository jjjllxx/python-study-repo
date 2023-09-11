"""
File: zhongwen.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-02-01 17:10:42
Function:


"""
import jieba

text = '这是一句用来测试的话'
a = "".join(list(jieba.cut(text)))
print(a)
