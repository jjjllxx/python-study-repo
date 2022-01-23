"""
File: 09.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-05 10:57:29
Function:


"""
import math

print('input equation ax^2+bx+c=0:')
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print('error!')
else:
    x1 = (-b + math.sqrt(delta)) / 2 / a
    x2 = (-b - math.sqrt(delta)) / 2 / a
    if x1 == x2:
        print("Solution of Equation：x1=x2=%.2f" % x1)
    else:
        print('Solution of Equation：x1=%.2f  x2=%.2f' % (x1, x2))
