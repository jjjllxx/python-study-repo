"""
File: 08.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-05 10:14:11
Function: judge leap year


"""

Year = int(input("Input Year: "))
isLeap = "Leap Year" if (Year % 4 == 0 and Year % 100 != 0) or (
            Year % 100 == 0 and Year % 400 == 0) else "Not Leap Year"
print("%d is %s" % (Year, isLeap))
