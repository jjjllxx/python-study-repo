"""
File: excell_2.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-05-25 16:05:30
Function:


"""
import openpyxl
wb = openpyxl.load_workbook(r'C:\Users\JLX\Desktop\douban.xlsx')
print(type(wb))
nws = wb.create_sheet(index=1, title='sheeeeet')