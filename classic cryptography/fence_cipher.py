"""
File: zhalan.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-08 20:56:22
Function:

Fence cipher encryption and decryption
Achieved: It can encrypt a piece of English characters, Chinese characters, numbers or other symbols, or a combination
of the above methods, and has a wide range of applications (but encrypted Chinese can be easily deciphered)
In the case that it is determined to be fence encryption but the fence width is unknown, brute force can be cracked,
and the iteration length is between 2 and 1/2 the length of the character to be deciphered.
Password disadvantage: easy to be deciphered (especially with spaces or Chinese characters)
Encryption and decryption are reciprocal (in the case of spaces, there may be small problems that do not affect reading,
such as conjunctions; or big problems: encrypted text, if spaces appear at the end or beginning, when copying
Missing a space causes the decryption to be garbled)
Multi-encryption, reverse input fence width when decrypting

栅栏密码加密与解密
已达成：可以加密一段英文字符、汉字、数字或其他符号，或以上多种方式混合的文字，适用范围广（但加密汉语很容易被破译）
在确定是栅栏加密但不知道栅栏宽度的情况下，可以暴力破解，迭代长度在2到二分之一待破译字符长之间
密码缺点：容易被破译（尤其是带空格或者汉字的情况下）
加密与解密互逆（在有空格的情况下可能会有不影响阅读的小问题，如连词;或者大问题：经过加密后的文字，如果空格出现在结尾或者开头，复制的时候
漏了一个空格导致解密成乱码）
可以多重加密，解密时逆向输入栅栏宽度

"""


def fence_coding(W, FLength):
    i = j = 0
    Fence = ''
    while i < FLength:
        while j + i < len(W):
            Fence += W[i + j]
            j += FLength
        i += 1
        j = 0
    print('Sentence after encryption: \n', Fence)  # 加密后的密文:


def fence_decoding(W, FLength):
    i = j = 0
    Fence = ''
    Fence_Width = len(W) // FLength + 1
    Fence_Extra = len(W) % FLength
    while i < Fence_Width:
        if i + 1 == Fence_Width:
            while j < Fence_Extra:
                Fence += W[i]
                j += 1
                i += Fence_Width
        else:
            while i + j < len(W):
                Fence += W[i + j]
                if j < Fence_Extra * Fence_Width:
                    j += Fence_Width
                else:
                    j += (Fence_Width - 1)
        i += 1
        j = 0
    print(f'When the width of fence is {FLength},Encoding result:\n{Fence}')  # 栅栏宽度为Flength时，解密的文字


Mod_Choice = input('Selection: 0.Encrypt 1.Decrypt 2. Unknown width,decrypt violently\n')  # 请选择：0.加密 1.解密 2.不知宽度,暴力解密:
Word_input = input('Sentence to encrypt/decrypt:\n')  # 请输入想要加/解密的文字：

if Mod_Choice == '0':
    Fence_Length = int(input('Please enter the width of fence:\n'))  # 请输入栅栏的宽度：
    fence_coding(Word_input, Fence_Length)

if Mod_Choice == '1':
    Fence_Length = int(input('Please enter the width of fence:\n'))  # 请输入栅栏的宽度：
    fence_decoding(Word_input, Fence_Length)

if Mod_Choice == '2':
    for k in range(2, len(Word_input)):
        fence_decoding(Word_input, k)
