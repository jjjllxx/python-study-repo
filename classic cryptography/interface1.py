"""
File: interface1.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-12 19:06:33
Function:


"""


def judge_out():
    input()
    judgejudge = input('press 5 to exit, any other keys to continue coding/encoding.')  # 按5退出，按其他任意键继续解密或加密
    return judgejudge


while True:
    mod_choice = input('Please select way to decrypt/encrypt: 0.Virginia/Caesar 1.Fence 2.Morse code '
                       '3.Nine-Key-keyboard 4.Qwe(26-keys): 5.Exit\n')
    # 请选择解密或加密方式: 0.弗吉尼亚和凯撒 1.栅栏加密 2.摩斯密码 3.九键 4.qwe 5.退出：
    if mod_choice == '0':
        print('User selected Virginia/Caesar')  # 用户选择了弗吉尼亚或凯撒
        import virginia_cipher
        if judge_out() == '5':
            break
        else:
            continue
    elif mod_choice == '1':
        print('User selected fence')  # 用户选择了栅栏
        import fence_cipher
        if judge_out() == '5':
            break
        else:
            continue
    elif mod_choice == '2':
        print('User selected Morse Code')  # 用户选择了摩斯密码
        import morse_code
        if judge_out() == '5':
            break
        else:
            continue
    elif mod_choice == '3':
        print('User selected 9-keys')  # 用户选择了九键
        import jiujian_transfer
        if judge_out() == '5':
            break
        else:
            continue
    elif mod_choice == '4':
        print('User selected QWE(26-keys)')  # 用户选择了qwe
        import qwe_transfer
        if judge_out() == '5':
            break
        else:
            continue
    elif mod_choice == '5':
        break
    else:
        print('Illegal operation, please key again')  # 非法，请重新选择
        continue
