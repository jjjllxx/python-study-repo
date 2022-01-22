"""
File: xiaoming.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-20 11:20:30
Function:


"""


class Human:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return '%s现在的体重是%.2fkg' % (self.name, self.weight)

    def running(self):
        self.weight -= 0.5

    def eating(self):
        self.weight += 1


xiaoming = Human('xiaoming', 75)
xiaohong = Human('xiaohong', 45)
xiaoming.eating()
xiaoming.running()
xiaohong.eating()
xiaohong.eating()
print(xiaohong)
print(xiaoming)
