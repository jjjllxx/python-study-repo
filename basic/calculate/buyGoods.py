"""
File: 07.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-05 09:55:38
Function:


"""
name = 'fentiao'
isBuy = True
goods = 'da'
if isBuy:
    if goods == 'knife' or goods == 'gun' or goods == 'poison':
        print('forbidden')
    else:
        print('allowed')
else:
    print('forbidden')
