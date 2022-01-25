"""
File: morse_code.py.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-10 17:48:15
Function:

Complete the function of converting Morse code into corresponding numbers or letters or digital letters into passwords,
suitable for different symbols of dots, dashes and intervals
To be improved: Some passwords are separated by more than one character, and some passwords have different interval
symbols between letters and letters, words and words.

完成摩斯密码转换成对应的数字或字母或者数字字母转换成密码的功能，适用于密码的不同的点、划、间隔符号
待改进：有的密码间隔不止一个字符，有的密码字母与字母，单词与单词的间隔符号不一致

"""


def Letter_transfer(Letter_Input, long_symbol, short_symbol):
    morse_code_dict = {'a': short_symbol + long_symbol, 'b': long_symbol + short_symbol * 3,
                       'c': (long_symbol + short_symbol) * 2, 'd': long_symbol + short_symbol * 2,
                       'e': short_symbol, 'f': short_symbol * 2 + long_symbol + short_symbol,
                       'g': long_symbol * 2 + short_symbol, 'h': short_symbol * 4,
                       'i': short_symbol * 2, 'j': short_symbol + long_symbol * 3,
                       'k': long_symbol + short_symbol + long_symbol,
                       'l': short_symbol + long_symbol + short_symbol * 2,
                       'm': long_symbol * 2, 'n': long_symbol + short_symbol,
                       'o': long_symbol * 3, 'p': short_symbol + long_symbol * 2 + short_symbol,
                       'q': long_symbol * 2 + short_symbol + long_symbol,
                       'r': short_symbol + long_symbol + short_symbol,
                       's': short_symbol * 3, 't': long_symbol,
                       'u': short_symbol * 2 + long_symbol, 'v': short_symbol * 3 + long_symbol,
                       'w': short_symbol + long_symbol * 2, 'x': long_symbol + short_symbol * 2 + long_symbol,
                       'y': long_symbol + short_symbol + long_symbol * 2, 'z': long_symbol * 2 + short_symbol * 2,
                       '5': short_symbol*5, '6': long_symbol+short_symbol*4, '7': long_symbol*2+short_symbol*3,
                       '8': long_symbol*3+short_symbol*2, '9': long_symbol*4+short_symbol, '0': long_symbol*5,
                       '1': short_symbol+long_symbol*4, '2': short_symbol*2+long_symbol*3,
                       '3': short_symbol*3+long_symbol*2, '4': short_symbol*4+long_symbol
                       }

    morse_decode_dict = {value: key for key, value in morse_code_dict.items()}

    if Letter_Input in morse_decode_dict.keys():
        return morse_decode_dict[Letter_Input]
    elif Letter_Input in morse_code_dict.keys():
        return morse_code_dict[Letter_Input]
    if Letter_Input == '/':
        return '/'
    if Letter_Input == ' ':
        return ''
    return ' '


def Morse_decoding(Input_str):
    long_sym = input('Please enter the symbol represent dash:')  # 请输入表示划的符号
    short_sym = input('Please enter the symbol represent dot:')  # 请输入表示点的符号
    interval_sym = input('Please enter the symbol represents interval:')  # 请输入表示间隔的符号
    Input_str += interval_sym
    word_str = ''
    Output_str = ''
    i = 0

    if long_sym not in Input_str:
        for i in range(len(Input_str)):
            Output_str += Letter_transfer(Input_str[i], long_sym, short_sym)
            Output_str += interval_sym
    else:
        while i < len(Input_str):
            if Input_str[i] == interval_sym and (Input_str[i - 1] == long_sym or Input_str[i - 1] == short_sym):
                Output_str += Letter_transfer(word_str, long_sym, short_sym)
                i += 1
                word_str = ''
            elif Input_str[i] == long_sym or Input_str[i] == short_sym:
                word_str += Input_str[i]
                i += 1
            else:
                Output_str += Input_str[i]
                i += 1

    print('Sentence after transferring:', Output_str)  # 转换后的文字为


Input_string = input('Enter the sentence to be transferred:')  # 请输入要转换的文字
Morse_decoding(Input_string)
