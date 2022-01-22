"""
File: duixiang.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-15 09:41:10
Function:


"""


class Cat:
    def eat(self):
        print(f'{self.name}爱吃鱼')

    def drink(self):

        print('小猫要喝水')


tom = Cat()
tom.name = 'tom'
tom.drink()
tom.eat()


print(tom.name)