"""
File: duixiang2.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-15 15:30:35
Function:


"""


class Cat:
    def __init__(self):
        print('这是一个初始化方法')
        new_name = input(':')
        self.name = new_name

    def eat(self):
        print(f'{self.name}爱吃鱼')

    def __del__(self):
        print('88')

    def __str__(self):
        return f'这是属于猫类的{self.name}'


tom = Cat()
tom.eat()

print(tom)
print('----------------')