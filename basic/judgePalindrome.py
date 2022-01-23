"""
File: string.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-06 09:50:54
Function:
judge whether a string is palindrome, only consider digit and letter, ignore lowercase or uppercase
判断一个字符串是不是回文串，只考虑字母和数字字符，可以忽略字母的大小写

"""

Input_string = str(input('please enter a string: '))  # 输入一个字符串
Test_string = ''
count = len(Input_string)
for i in range(count):
    if 'A' <= Input_string[i] <= 'Z' or 'a' <= Input_string[i] <= 'z' or '0' <= Input_string[i] <= '9':
        Test_string += Input_string[i]
    else:
        continue
print('string after arrange: ', Test_string)  # string after arrange
count = len(Test_string)
j = 0
while j <= (count//2):
    if Test_string[j] == Test_string[-1-j] or ord(Test_string[j]) == (ord(Test_string[-1-j]) + 32) or ord(Test_string[j]) == (ord(Test_string[-1-j]) - 32):
        j += 1
        continue
    else:
        break
print('Palindrome：', j == (count//2 + 1))  # 是否回文



