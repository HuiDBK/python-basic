# Python基本语法概览

## 引言

> 这里将罗列一些 `Python` 的基本语法，让初学者对 **Python语法** 有一个整体的概念。

<br/>

## Python 注释

### 单行注释

> 以 `#` 开头，`#` 右边的所有东西都被当做说明文字，而不是真正要执行的程序，只起到辅助说明作用

```Python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 这是第一个单行注释
print('hello python')

print('hello world')	# 第二个单行注释
```

<br/>

### 多行注释

在 `Python` 程序中使用多行注释，可以用 **一对连续的三个引号**(单引号 `''` 和 双引号 `""` 都可以)

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
这是一个多行注释
输入hello hui
"""
print('hello hui')
```

<br/>

## 标识符

> 标识符就是程序员定义的 **变量名、函数名、类名**等。

<br/>

- 标识符可以由 **字母**、**下划线_** 和 **数字** 组成
- **不能以数字开头**
- 标识符对大小写敏感

<br/>

## Python 关键字

> - **关键字** 就是在 `Python` 内部已经使用的标识符
> - **关键字** 具有特殊的功能和含义

<br/>

`Python 3.7.9` 版本所有关键字如下所示：

```python
'False', 'None', 'True', 'and', 'as', 'assert', 'async', 

'await', 'break', 'class', 'continue', 'def', 'del', 

'elif', 'else', 'except', 'finally', 'for', 'from', 

'global', 'if', 'import', 'in', 'is', 'lambda', 

'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 

'try', 'while', 'with', 'yield'
```

<br/>

## Python 简单数据类型

- 字符串类型 `str`
- 整数类型 `int`
- 浮点数类型 `float`

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 字符串类型变量
name = 'hui'

# 整数类型变量
age = 21

# 浮点数类型变量
price = 520.1314

```

<br/>

## Python 运算符初步了解

### 算术运算符

|  运算符  |  描述  | 实例                                            |
| :------: | :----: | ----------------------------------------------- |
| **`+`**  |   加   | **3 + 6**                                       |
| **`-`**  |   减   | **10 - 5**                                      |
| **`*`**  |   乘   | **10 * 20**                                     |
| **`/`**  |   除   | **10 / 20**                                     |
| **`//`** | 取整除 | 返回除法的整数部分（商） **9 // 2**  输出结果 4 |
| **`%`**  | 取余数 | 返回除法的余数  **9 % 2**                       |
| **`**`** |   幂   | 又称次方、乘方，**2 \*\* 3**                    |

<br/>

### 比较运算符

假设 `x=20`，`y=30`

| 运算符   | 描述     | 实例                |
| -------- | -------- | ------------------- |
| **`==`** | 等于     | (a == b) 返回 False |
| **`!=`** | 不等于   | (a != b) 返回 True  |
| **`>`**  | 大于     | (a > b) 返回 False  |
| **`<`**  | 小于     | (a < b) 返回 True   |
| **`>=`** | 大于等于 | (a >= b) 返回 False |
| **`<=`** | 小于等于 | (a <= b) 返回 True  |

<br/>

### 赋值运算符

| 运算符    | 描述                       | 实例                                  |
| --------- | -------------------------- | ------------------------------------- |
| **`=`**   | 简单的赋值运算符           | c = a + b 将 a + b 的运算结果赋值为 c |
| **`+=`**  | 加法赋值运算符             | c += a  等效于  c = c + a             |
| **`-=`**  | 减法赋值运算符             | c -= a   等效于  c = c - a            |
| **`*=`**  | 乘法赋值运算符             | c *= a   等效于  c = c * a            |
| **`/=`**  | 除法赋值运算符             | c /= a   等效于  c = c / a            |
| **`//=`** | 取整除赋值运算符           | c //= a  等效于  c = c // a           |
| **`%=`**  | 取 **模** (余数)赋值运算符 | c %= a  等效于  c = c % a             |
| **`**=`** | 幂赋值运算符               | `c **= a` 等效于` c = c** a`          |

<br/>

### 逻辑运算符

| 运算符    | 逻辑表达式 | 描述                                                         |
| :-------- | :--------- | :----------------------------------------------------------- |
| **`and`** | `x and y`  | **布尔"与"** - 如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值。 |
| **`or`**  | `x or y`   | **布尔"或"** - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。 |
| **`not`** | `not x`    | **布尔"非"** - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 |

<br/>

`Python` 中还有一下其他运算符，这里就不一一列举，后面会有专门一篇对Python运算符进行测试讲解

- 位运算符
- 成员运算符
- 身份运算符

<br/>

## Python 分支结构

### 单个 if 判断

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

name = 'hui'

if name == 'hui':
    print('my name is hui')
    
# 输出结果为：my name is hui    
```

<br/>

### if ... else ... 判断

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

age = 21

if age < 23:
    print('小姐姐')
else:
    print('美女姐姐')
    
# 输出结果为：小姐姐       
```

<br/>

### if ... elif ... else 判断

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

score = 85

if score < 60:
    print('不及格')
elif score < 70:
    print('及格')
elif score < 80:
    print('中等')
elif score < 90:
    print('良好')
else:
    print('优秀')
    
# 输出结果为：良好    
```

<br/>

## Python 循环结构

> Python中有两个循环结构分别为
>
> - for 循环
> - while 循环

<br/>

### for 循环

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

for i in range(3):
    print(i)
   
# 结果如下
# 0
# 1
# 2
```

<br/>

### while 循环

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 100以内的和
result = 0

# 定义一个整数的变量记录循环的次数
i = 0

# 开始循环
while i <= 100:

    result += i
    i += 1
    
print(result)	# 结果为：5050
```

<br/>

## Python 函数

### 函数的定义

```python
def 函数名():
    
    函数体
    ……
    
例如:
def hello():
    print('hello python')
    
```

<br/>

### 函数的调用

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

name = 'ithui'

def say_hello():
    print("hello 1")
    print("hello 2")
    print("hello 3")
    
print(name)

say_hello()

# 输出结果为：
# ithui
# hello 1
# hello 2
# hello 3
```

<br/>

### 函数传参的使用

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

a = 10
b = 20

def sum(x, y):
    z = x + y
    print(z)

sum(a, b)	# 输出 30    
```

<br/>

## Python 高级数据类型

### 列表 list

> - `list`（列表） 是 `Python` 中使用 **最频繁** 的数据类型，在其他语言中通常叫做 **数组**
> - 列表用 `[]` 定义，**数据** 之间使用 `,` 分隔
> - 可以通过 **索引** 获取元素如 `[0]` ，索引也可以叫为 **下标**

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

li = [1, 2, 3, 4, 5]

# 打印列表
print(li)	# [1, 2, 3, 4, 5]

# 获取列表第0个元素
print(li[0])	# 1
```

<br/>

### 元组 tuple

> - `Tuple`（元组）与列表类似，不同之处在于元组的 **元素不能修改**
> - 元组用 `()` 定义，**数据** 之间使用 `,` 分隔
> - 通过 **索引** 获取元素

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

t = (1, 2, 3)

# 打印元组
print(t)	# (1, 2, 3)

# 获取元组第0个元素
print(t[0])	# 1
```

<br/>

### 字典 dict

> - `dict`（字典） 是 **除列表以外** `Python` 之中 **最灵活** 的数据类型
> - 字典用 `{}` 定义
> - 字典使用 **键值对** 存储数据，键值对之间使用 `,` 分隔

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

person = {
    'name': 'hui',
    'age': 21,
    'gender': True,
    'height': 1.75
}

# 根据对应的键key获取值
print(person['name'])    	# hui
print(person['age'])    	# 21
print(person['gender'])    	# True
print(person['height'])    	# 1.75
```

<br/>

### 集合 set

> - `set`（集合） 与列表类似，不同之处在于集合的 **元素不重复**
> - 集合也是用 `{}` 定义，但元素之间使用 `,` 分隔 

```Python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

name_set = {'hui', 'wang', 'zack', 'hui'}

print(name_set)    	# 结果为 {'hui', 'wang', 'zack'}

```

<br/>

## Python 类

> 类，用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。Python中使用 `class` 关键字定义类

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 定义类
class User:
    
    # 类属性
    name = 'hui'
    age = 21
    
    # 方法
    def get_age(self):
        print(self.age)
        return self.age

# 创建类对象    
user = User()

# 访问类的属性和方法
print(user.name)
user.get_age()
```

<br/>

## 尾语

**✍ 用  Code 谱写世界，让生活更有趣。❤️**

**✍ 万水千山总是情，点赞再走行不行。❤️**

**✍ 码字不易，还望各位大侠多多支持。❤️**

<br/>

![007.jpg](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9186c975981643ada4cae7d9c12db2f8~tplv-k3u1fbpfcp-watermark.image)
