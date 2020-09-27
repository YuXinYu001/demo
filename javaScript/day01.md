# javaScript基础

* javaScript的用法

  HTML中的脚本必须放在"<script>与</script>"标签之间，脚本可被放置在HTML的<body>和<head>部分中。可以将javaScript保存到外部文件中，扩展民是.js，如需使用外部文件，在<script>的src属性中设置改.js文件

  如：

  ```html
  <!DOCTYPE html>
  <html>
      <body>
          <script src="myScript.js"></script>
      </body>
  </html> 
  ```
  
* javaScript输出

  javaScript没有任何打印或者输出的函数。javaScript可以通过不同的方式来输出数据：

  * 使用window.alert()弹出警告框。
  * 使用document.write()方法将内容写到HTML文档中。
  * 使用innerHTML写入HTML元素
  * 使用console.log()写入到浏览器的控制台。

* javaScript语法

  javaScript是一个脚本语言。它是一个轻量级，但功能强大的编程语言。

  * javaScript字面量

    ​	固定值称为字面量。如3.14。

    数字字面量可以是整数或者是小数，或者是科学计数（e）。如：3.14  1001, 123e5

    字符串字面量可以使用单引号或者双引号。如：“hello js ” 'hello js'

    表达式字面量用于计算:5+6  5*6

    数组字面量定义一个数组：[40, 50, 100, 10]

    对象字面量定义一个对象：{firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"}

    函数字面量定义一个函数：function myFunction(a,b){return a*b}

  * javaScrpt变量

    javaScript使用关键字var来定义变量，使用'='来为变量赋值。变量可以通过变量名访问，在指令式语言中，变量通常是可变的，字面量是一个恒定的值。

  * javaScript操作符

    javaScript使用算数运算符来计算值。使用赋值运算符来给变量赋值。基本C语言中的运算符在javaScript中都差不多。

  * javaScript语句

    在HTML中，javaScript语句向浏览器发出指令。语句用西文字符的分号分隔。

  * javaScript关键字

    javaScript关键字用于标识要执行的操作。

  此外javaScript对大小写是敏感的。javaScript使用Unicode字符集。

* javaScript语句

  * javaScript语句标识符

  | 语句         | 描述                                                         |
  | :----------- | :----------------------------------------------------------- |
  | break        | 用于跳出循环。                                               |
  | catch        | 语句块，在 try 语句块执行出错时执行 catch 语句块。           |
  | continue     | 跳过循环中的一个迭代。                                       |
  | do ... while | 执行一个语句块，在条件语句为 true 时继续执行该语句块。       |
  | for          | 在条件语句为 true 时，可以将代码块执行指定的次数。           |
  | for ... in   | 用于遍历数组或者对象的属性（对数组或者对象的属性进行循环操作）。 |
  | function     | 定义一个函数                                                 |
  | if ... else  | 用于基于不同的条件来执行不同的动作。                         |
  | return       | 退出函数                                                     |
  | switch       | 用于基于不同的条件来执行不同的动作。                         |
  | throw        | 抛出（生成）错误 。                                          |
  | try          | 实现错误处理，与 catch 一同使用。                            |
  | var          | 声明一个变量。                                               |
  | while        | 当条件语句为 true 时，执行语句块。                           |

  * javaScript数据类型

    **值类型(基本类型)**：字符串（String）、数字(Number)、布尔(Boolean)、对空（Null）、未定义（Undefined）、Symbol。

    **引用数据类型**：对象(Object)、数组(Array)、函数(Function)

    javaScript拥有动态类型。这意味着相同变量可用作不同的类型。javaScript变量均为对象。当声明一个变量时就创建了一个新的对象。