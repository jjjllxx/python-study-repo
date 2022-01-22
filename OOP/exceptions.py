"""
File: yichang.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-22 20:41:05
Function:


"""
while True:
    try:
        num = int(input('please enter a number: '))
        out1 = 8/num
    except ValueError:
        print('please retry')
        continue
    except Exception as result:
        print('error: %s' % result)
        continue
    else:
        print('no error')
        break
    finally:
        print('anyway')