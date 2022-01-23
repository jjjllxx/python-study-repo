"""
File: 12.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-05 15:49:45
Function:


"""

name = 'root'
passwd = 'westos'
count = 0
while count < 3:
    name1 = input('Please Enter Your Name:')
    passwd1 = input('Please Enter Your Password:')
    if name1 == name and passwd == passwd1:
        print()
        print('Welcome!')
        break
    else:
        count += 1
        if count == 3:
            break
        print()
        print('Error!Please Retry!You Still Have', 3-count, 'Chance(s).')
        print()
print('You Account is Locked!') if count == 3 else print()
input()




