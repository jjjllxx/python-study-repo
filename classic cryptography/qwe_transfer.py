"""
File: qwe_transfer.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-12 16:12:46
Function:


"""

qwe_code = {'q': 'a', 'w': 'b', 'e': 'c', 'r': 'd', 't': 'e', 'y': 'f', 'u': 'g', 'i': 'h', 'o': 'i',
            'p': 'j', 'a': 'k', 's': 'l', 'd': 'm', 'f': 'n', 'g': 'o', 'h': 'p', 'j': 'q', 'k': 'r',
            'l': 's', 'z': 't', 'x': 'u', 'c': 'v', 'v': 'w', 'b': 'x', 'n': 'y', 'm': 'z', ' ': ' '}
qwe_decode = {value: key for key, value in qwe_code.items()}

Input_str = input('Enter the sentence to be transferred:')  # 请输入要转换的文字
VInput_str = Input_str.lower()
Output_str = ''
for i in range(len(Input_str)):
    if VInput_str[i] in qwe_code.values():
        Output_str += qwe_code[VInput_str[i]]
    else:
        Output_str += VInput_str[i]
print('Result of qwe-decryption:', Output_str)  # qwe解密的结果为
Output_str = ''
for i in range(len(Input_str)):
    if VInput_str[i] in qwe_code.values():
        Output_str += qwe_decode[VInput_str[i]]
    else:
        Output_str += VInput_str[i]
print('Result of qwe-encryption:', Output_str)  # qwe加密的结果为
