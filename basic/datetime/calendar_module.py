"""
File: rili.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-03-24 19:32:06
Function:


"""
import time
for i in range(3):
    print(i)
    t1 = time.time()
    time.sleep(1)
    t2 = time.time()
    print(t2-t1)