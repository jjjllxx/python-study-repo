"""
File: yichangchuandi.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-23 08:15:49
Function:


"""


def input_password():
    pwd = input('please set your password: ')
    if len(pwd) >= 8:
        return pwd
    else:
        print('raise exception')
        ex = Exception('the password is too short')
        raise ex


try:
    print(input_password())
except Exception as result:
    print(result)