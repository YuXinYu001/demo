#!/usr/bin/python3
# -*- cocing: utf-8 -*-

def trim(s):
    if(s[0:1] != ' ' and s[-1:] != ' '):
        return s
    if(s[0:1] == ' '):
        s = s[1:]
    if(s[-1:] == ' '):
        s = s[0:-1]
    return trim(s)


#测试用例
if(trim("  hello   ") != 'hello'):
    print("测试失败！")
elif(trim(" hello") != 'hello'):
    print("测试失败!")
elif(trim("hello  ") != 'hello'):
    print("测试失败！")
elif(trim("  hello word  ") != 'hello word'):
    print("测试失败！")
else:
    print("测试成功")
