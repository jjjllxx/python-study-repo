"""
File: 05.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-05 08:30:36
Function:


"""

import math

Radius: float = float(input("Input Radius: "))
Circumference = 2 * math.pi * Radius
Area = math.pi * Radius ** 2
print("Radius is %.2f,perimeter is %.2f,area is %.2f." % (Radius, Circumference, Area))
