"""
File: 11.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-05 14:14:30
Function:


"""
# for item in 'hello':
#     if item == 'l':
#         continue
#     else:
#         print(item)

for a in range(1, 10, 1):
    for b in range(1, a+1):
        print(b, 'x', a, '=%-2.d' % (a*b), end=' ')
    print()


