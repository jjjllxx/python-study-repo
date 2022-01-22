"""
File: lei.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-21 20:41:40
Function:


"""


class Tool(object):
    count = 0

    @classmethod
    def show_tool_count(cls):
        print('the number of tool is', cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool('hammer')
tool2 = Tool('bottle')
tool3 = Tool('knife')

tool3.count = 99
print(Tool.count)
Tool.show_tool_count()
tool3.show_tool_count()