"""
File: idcheck.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-06 14:28:40
Function:
check whether is a valid python identifier
a valid identifier must start wth letter or underscore and only has digit/letter/underscore
only check identifier with length of over 2

检查Python有效标识符的脚本
Python标识符必须以字母或下划线开头/只检查长度大于或等于2的标识符/以字母或者下划线开始/后面要跟字母下划线或者数字
"""
Input_flag = input('please enter an identifier:')
while 1:
    if len(Input_flag) < 2:
        Input_flag = input('the identifier is too short, please enter again:')
        continue
    else:
        break
i = 0
if Input_flag[0] == '_' or 'a' <= Input_flag[0] <= 'z' or 'A' <= Input_flag[0] <= 'Z':
    for i in range(len(Input_flag)):
        if Input_flag[i] == '_' or 'a' <= Input_flag[0] <= 'z' or 'A' <= Input_flag[0] <= 'Z' or '0' <= Input_flag[0] <= '9':
            continue
        else:
            break
print('Identifier: ', i == len(Input_flag) - 1)



