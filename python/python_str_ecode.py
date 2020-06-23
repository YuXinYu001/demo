#!/usr/bin/python3
# -*- coding: utf-8 -*-

print("中文测试str")

cassmast = ['micheel', 'Bod', 'boom' ]
print(cassmast)

print('cassmast len = ', len(cassmast))
print('cassmast[0] = ', cassmast[0])
print('cassmast[1] = ', cassmast[1])
print('cassmast[-1] = ', cassmast[-1])
cassmast.append('trecy')
print('cassmast.append(\'trecy\')', cassmast)

cassmast.insert(1, "jack")
print(cassmast)

cassmast.pop()
print(cassmast)

cassmast.pop(1)
print(cassmast)

a = 255
print(hex(a))
