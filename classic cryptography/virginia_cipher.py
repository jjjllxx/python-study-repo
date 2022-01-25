"""
File: miyao_c.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-08 13:16:02
Function:

Virginia cipher encryption and decryption
Achieved: English characters can have spaces, encryption and decryption are reversed
To be improved: cannot be used to encrypt non-English characters (numbers and Chinese punctuation marks),
all upper and lower case will be converted to lower case
Advantage: almost impossible to crack without the key

弗吉尼亚密码加密与解密
已达成：英文字符可以带空格，加密解密互逆
待改进：不能用于加密非英语字符（数字与汉字标点符号），会把大小写全部转换为小写
密码优点：没有秘钥的情况下几乎不能被破解
"""

import string


def virginia_coding(code_string, key_string):
    vcode_string = code_string.lower()
    vkey_string = key_string.lower()
    after_str = ''
    i = j = 0
    while i < len(vcode_string):
        if j > len(vkey_string) - 1:
            j = 0
        if vcode_string[i] == ' ' or vkey_string[j] == ' ':
            after_str += vcode_string[i]
            i += 1
            j += 1
            continue
        else:
            Next_Asc = ord(vcode_string[i]) + ord(vkey_string[j]) - 97
            if Next_Asc > 122:
                Next_Asc -= 26
            after_str += chr(Next_Asc)
            i += 1
            j += 1
            if j > len(vkey_string) - 1:
                j = 0
    print('Sentence after encryption:', after_str)  # 加密后的密文为


def virginia_decoding(code_string, key_string):
    vcode_string = code_string.lower()
    vkey_string = key_string.lower()
    after_str = ''
    i = j = 0
    while i < len(vcode_string):
        if j > len(vkey_string) - 1:
            j = 0
        if vcode_string[i] == ' ' or vkey_string[j] == ' ':
            after_str += vcode_string[i]
            i += 1
            j += 1
            continue
        Next_Asc = ord(vcode_string[i]) - ord(vkey_string[j]) + 97
        if Next_Asc < 97:
            Next_Asc += 26
        after_str += chr(Next_Asc)
        i += 1
        j += 1
    print('Sentence after decryption:', after_str)  # 解密后的明文为


while True:
    mode_choice = input('Please select:0.Virginia encryption 1.Virginia decryption 2.Caesar encryption 3.Caesar '
                        'decryption 4.Violent Caesar decryption\n')
    # 请选择:0.弗吉尼亚加密 1.弗吉尼亚解密 2.凯撒加密 3.凯撒解密 4.暴力凯撒解密
    if mode_choice in '01234':
        break
    else:
        print('Please enter again')  # 请重新输入

code_str = input('Please enter the text:')  # 请输入文本

if mode_choice == '0':
    key_str = input('Please enter the key:')  # 请输入秘钥
    virginia_coding(code_str, key_str)
    input()

if mode_choice == '1':
    key_str = input('Please enter the key:')  # 请输入秘钥
    virginia_decoding(code_str, key_str)
    input()

if mode_choice == '2':
    Caesar_chr = chr(int(input('Please enter the offset:\n')) + 97)  # 请输入位移量
    virginia_coding(code_str, Caesar_chr)
    input()

if mode_choice == '3':
    Caesar_chr = chr(int(input('Please enter the offset:\n')) + 97)  # 请输入位移量
    virginia_decoding(code_str, Caesar_chr)
    input()

if mode_choice == '4':
    i = 97
    while i < 123:
        print(f'When offset is{i - 97},', end='')  # 这是位移量为 时的结果:
        virginia_decoding(code_str, chr(i))
        i += 1
    input()
