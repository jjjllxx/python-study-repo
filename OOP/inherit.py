"""
File: jicheng.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-21 11:15:48
Function:


"""


class Animal(object):
    @staticmethod
    def Eat():
        print('eat')

    @staticmethod
    def drink_water():
        print('drink')

    @staticmethod
    def sleep():
        print('sleep')

    @staticmethod
    def running():
        print('run')


class Dog(Animal):
    def bark(self):
        print('bark')


class Xiaotianquan(Dog):
    @staticmethod
    def fly():
        print('fly')

    def bark(self):
        print('dgasjkdhg')


tom = Dog()
tom.sleep()
xtq = Xiaotianquan()
xtq.bark()
