"""
File: 03.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-04 15:15:32
Function:


"""
Student_Name = input("Student Name:")
Chinese_Grate = int(input("Chinese Grate:"))
Math_Grate = int(input("Math Grate:"))
English_Grate = int(input("English Grate:"))
Total = Chinese_Grate + Math_Grate + English_Grate
Average = Total / 3
print("Student Name: %s Total:%d Average: %.2f points." % (Student_Name, Total, Average))
input()
