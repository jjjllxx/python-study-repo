"""
File: soldier.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-20 16:47:37
Function:


"""


class Gun:
    def __init__(self, name, bullet_num):
        self.name = name
        self.bullet = bullet_num

    def fire(self, fire_num):
        if self.bullet - fire_num < 0:
            print('run out')
            self.bullet = 0
        else:
            self.bullet -= fire_num

    def __str__(self):
        return f'{self.name}剩{self.bullet}发子弹'


class Soldier:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def shoot(self, num):
        self.gun.fire(num)

    def reload(self, num):
        self.gun.bullet += num

    def __str__(self):
        return f'{self.name}有一把{self.gun.name}，剩{self.gun.bullet}发子弹'


if __name__ == '__main__':
    ak47 = Gun('ak47', 30)
    ray = Soldier('ray', ak47)
    ray.shoot(35)
    ray.reload(20)
    print(ray)
    print(ak47)
