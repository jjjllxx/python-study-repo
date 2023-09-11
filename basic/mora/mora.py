"""
File: caiquan.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-07 16:44:52
Function:
mora with computer
与电脑猜拳
mora with computer
封装语句：pyinstaller -F -i yinghua.ico mora.py  (pack into .exe file)

to be developed: artificial intelligence
待开发功能：智能化电脑出拳，用来测试什么出拳策略最优

"""


def sakura():
    import turtle as T
    import random
    import time

    # 画樱花的躯干(60,t)
    def Tree(branch, t):
        time.sleep(0.0005)
        if branch > 3:
            if 8 <= branch <= 12:
                if random.randint(0, 2) == 0:
                    t.color('snow')  # 白
                else:
                    t.color('lightcoral')  # 淡珊瑚色
                t.pensize(branch / 3)
            elif branch < 8:
                if random.randint(0, 1) == 0:
                    t.color('snow')
                else:
                    t.color('lightcoral')  # 淡珊瑚色
                t.pensize(branch / 2)
            else:
                t.color('sienna')  # 赭(zhě)色
                t.pensize(branch / 10)  # 6
            t.forward(branch)
            a = 1.5 * random.random()
            t.right(20 * a)
            b = 1.5 * random.random()
            Tree(branch - 10 * b, t)
            t.left(40 * a)
            Tree(branch - 10 * b, t)
            t.right(20 * a)
            t.up()
            t.backward(branch)
            t.down()

    # 掉落的花瓣
    def Petal(m, t):
        for i in range(m):
            a = 200 - 400 * random.random()
            b = 10 - 20 * random.random()
            t.up()
            t.forward(b)
            t.left(90)
            t.forward(a)
            t.down()
            t.color('lightcoral')  # 淡珊瑚色
            t.circle(1)
            t.up()
            t.backward(a)
            t.right(90)
            t.backward(b)

    # 绘图区域
    t = T.Turtle()
    # 画布大小
    w = T.Screen()
    t.hideturtle()  # 隐藏画笔
    t.getscreen().tracer(5, 0)
    w.screensize(bg='wheat')  # wheat小麦
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color('sienna')

    # 画樱花的躯干
    Tree(60, t)
    # 掉落的花瓣
    Petal(200, t)
    w.exitonclick()


def game_show(a):
    if a == 1:
        return '石头'
    elif a == 2:
        return '剪刀'
    elif a == 3:
        return '布'
    else:
        return '非法'


# 将数字转换成汉字

def judge_digits(b, num0=0, num1=9):
    while True:
        a = input(b)
        if len(a) != 1:
            print('请重新输入一个数字')  # please enter a number
            continue
        elif ord(a) > 48 + num1 or ord(a) < 48 + num0:
            print('请重新输入一个数字')
            continue
        else:
            break
    return int(a)


# 用于输入的函数，确保只输入一位数字。b为字符串输入的提示部分,num0,num1用于设置数字的上下限

def caiquan(Round=10001):
    import random
    win = 0
    lose = 0
    draw = 0
    i = 0
    while i < Round:
        Player_Choice = judge_digits('请输入选择：1.石头 2.剪刀 3.布 4.退出\n', 1, 4)
        if Player_Choice == 4:
            break
        Computer_Choice = random.randint(1, 3)
        print('玩家选择', game_show(Player_Choice), ',电脑选择', game_show(Computer_Choice))
        if Player_Choice < Computer_Choice or (Player_Choice == 3 and Computer_Choice == 1):
            print('玩家获胜！', end='')
            win += 1
            i += 1
            if win == (Round + 1) / 2:
                break
        elif Player_Choice == Computer_Choice:
            print('平局！', end='')
            draw += 1
            if Round == 10001:
                i += 1
        else:
            print('电脑获胜！', end='')
            lose += 1
            i += 1
        if Round == 10001:
            print(f'已经进行{i}局')
        else:
            print('还剩', Round - i, '局')

    if Round == 10001:
        print()
        print(f'玩家选择退出，游戏结束，玩家获胜{win}次，输{lose}次，平局{draw}次')
    else:
        if win == (Round + 1) / 2:
            print('\n乐轩恭喜您获胜啦！')
            sakura()
        else:
            print('\n呜呜呜，乐轩嘲笑您失败啦')


print('@乐轩制作')

Choice_Mod = judge_digits('请选择模式：1.固定局数（获胜会有彩蛋） 2.无尽模式（挑战人类意志） 3.作弊模式(暂未开发)\n', 1, 3)

if Choice_Mod == 3:
    print('暂未开发，敬请期待：）')
    input()

if Choice_Mod == 1:
    Choice_Round = judge_digits('请选择局数：1.三局两胜 2.五局三胜 3.七局四胜\n', 1, 3)
    caiquan((2 * Choice_Round + 1))
    input()

if Choice_Mod == 2:
    caiquan()
    input()
