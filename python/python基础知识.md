# python数据类型和变量
​		python中的数据类型和其他语言中的的数据类型相同，分别是：整数类型，浮点数类型，字符串类型，布尔类型，空值。

​		其中布尔类型支持and(与运算)，or(或运算)， not(非运算，单目运算符)，布尔类型的取值为True/False首字母必须大写。

​		空值是python中的一个特殊的值用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

​		此外python还提供了列表，字典等多种数据类型，还允许创建自定义数据类型。

​		在python中通常使用全大写字符表示常量，如通用的数学常量π在python中使用

```pyth
PI=3.1415926
```

来表示，事实上PI任然是一个变量，python根本没有任何机制保证PI不被改变。用全部大写的变量名表示常量只是一种习惯性的用法。

## 1.1 list(列表)

​		list是python内置的一种数据类型。它是一种有序的集合，可以随时添加，删除，修改元素。相当于数据结构中的链表。

​		可以像C语音中访问数组中某个元素的方式来访问list中的元素。当使用-1做索引的时候直接访问最后一个元素。

​		采用直接给元素赋值的方式改变元素的值。list里的数据类型可以不相同

​		如：

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

cassmast = ['micheel', 'Bod', 'tracy']
#可以使用len()函数获取list的元素个数
print("cassnast len = ", len(cassmast))
#访问list某个位置的元素
print('cassmast[0] = ', cassmast[0])
print("cassmast[1] = ", cassmast[1])
#可以使用append()函数往list最后添加元素
print("cassmast.append(\'boom\') =", cassmast.append('boom'))

#可以使用insert()函数在某个位置插入元素
cassmast.insert(1, 'jack')
print(cassmast)

#可以使用pop()函数删除最后的元素，或者使用pop(index)删除指定位置的元素
cassmast.pop()
print(cassmast)
cassmast.pop(1)
print(cassmast)

```

## 1.2 tuple（元组）

 		tuple也是python中内置的一种数据类型，和list非常类似，但是tuple一旦初始化就不能修改，只能访问。

# 条件判断

```python
#如果有多个判断条件可以使用or/and来进行
if (判断条件1 ):
    执行语句1
elif(判断条件2):
    执行语句2
    ……
else
	执行语句……
```

# 高级特性

## 3.1 切片

```python
L = list(range(100))
#取前n个元素
L[:n]
#取后n个元素
L[-n:]
#取前n-m个元素
L[n-1:m]
#前n个元素每隔m个元素取一个
L[:n:m]
#所有元素每隔n个元素取一个
L[::n]
```

字符串也可以看成是一个list，每个元素就是一个字符，因此字符串也可以使用切片操作，操作结果任然是字符串。

练习：利用切片操作实现trim(s)函数，去除字符串首尾的空格。

```python
#/usr/bin/pythom3
# -*- coding: utf-8 -*- 
def trim(s):
    if(s[0:1] != ' ' and s[-1:] != ' '):
        return s
    if(s[0:1] == ' '):
     	s=s[1:]
    if(s[-1:] == ' '):
        s=[0:-1]
    return trim(s)

if(trim("  hello   ") != 'hello'):
    print("测试失败！")
elif(trim(" hello") != 'hello'):
    print("测试失败!")
elif(trim("hello  ") != 'hello'):
    print("测试失败！")
else:
    print("测试成功")
```

## 3.2 迭代

如果给定一个list或tuple，我们可以通过`for`循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

   	python的for循环不仅可以作用于list和tuple上，也可以用于其他可迭代对象上，比如dict就可以迭代，默认情况下dict迭代的是key。如果要迭代value，可以用for v in d.values()，如果需要同时迭代key和value，可以使用        for k,v in d.items()。

​		如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

```python
>>> from collections.abc import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False
#collections模块在3.3版本之后被弃用了，如果需要使用其中的内容可以包含collections.abc
DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3, and in 3.9 it will stop working
```

