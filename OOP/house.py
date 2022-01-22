"""
File: house.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-20 14:36:59
Function:


"""


class Furniture:
    def __init__(self, name, area):
        self.area = area
        self.name = name

    def __str__(self):
        return '%s占地%.2f平方米' % (self.name, self.area)


class House:
    def __init__(self, name, area):
        self.area = area
        self.name = name
        self.FurnitureList = []
        self.remain_area = self.area

    def PutFurniture(self, furniture):
        self.remain_area -= furniture.area
        self.FurnitureList.append(furniture.name)

    def __str__(self):
        return f'{self.name}总面积{self.area}平方米，有{self.FurnitureList}，剩余面积{self.remain_area}平方米'


bed = Furniture('bed', 4)
print(bed)
chest = Furniture('chest', 2)
table = Furniture('table', 1.5)

xiaomingfangzi = House('xiaoming', 20)
xiaomingfangzi.PutFurniture(bed)
xiaomingfangzi.PutFurniture(chest)
xiaomingfangzi.PutFurniture(table)
print(xiaomingfangzi)