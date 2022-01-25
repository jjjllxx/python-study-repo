"""
File: jiujian_transfer.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-12 17:04:34
Function:


"""
import string

jiujian_code = {'a': '21', 'b': '22', 'c': '23', 'd': '31', 'e': '32', 'f': '33', 'g': '41', 'h': '42', 'i': '43',
                'j': '51', 'k': '52', 'l': '53', 'm': '61', 'n': '62', 'o': '63', 'p': '71', 'q': '72', 'r': '73',
                's': '74', 't': '81', 'u': '82', 'v': '83', 'w': '91', 'x': '92', 'y': '93', 'z': '94'}
jiujian_decode = {value: key for key, value in jiujian_code.items()}

Input_str = input('Please enter the sentence to transfer:')  # 请输入要转换的文字
Word_str = ''
Output_str = ''
print(Input_str[0] in string.digits)
if Input_str[0] in string.ascii_letters:
    for i in range(len(Input_str)):
        Output_str += jiujian_code[Input_str[i]]
    print('Result of 9-key coding:', Output_str)  # 九键加密的结果

if Input_str[0] in string.digits:
    for i in range(0, len(Input_str), 2):
        Word_str += (Input_str[i] + Input_str[i + 1])
        Output_str += jiujian_decode[Word_str]
        Word_str = ''
    print('Result of 9-key decoding:', Output_str)  # 九键解密的结果
