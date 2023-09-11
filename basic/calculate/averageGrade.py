"""
File: 06.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-05 08:52:13
Function:


"""
Input_Average = float(input("Average Grade:"))
if Input_Average > 100 or Input_Average < 0:
    Grade = 'illegal average grade'
elif 85 <= Input_Average:
    Grade = "A"
elif Input_Average >= 70:
    Grade = "B"
elif Input_Average >= 60:
    Grade = "C"
else:
    Grade = "D"
print("Average grade of student is %.1f，rank is %s。" % (Input_Average, Grade))
