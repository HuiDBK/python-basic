# Python 变量的基本使用

## 引言

> **程序就是用来处理数据的，而变量就是用来存储数据的**

<br/>

## 一、变量定义

- 在 Python 中，每个变量 **在使用前都必须赋值**，变量 **赋值以后** 该变量 **才会被创建**
- 等号 `=` 用来给变量赋值
  - `=` 左边是一个变量名
  - `=` 右边是存储在变量中的值

```python
name = 'hui'
```

> 变量定义之后，后续就可以直接使用了

<br/>

### 1）变量演练1 —— IPython

```python
In [1]: name = 'hui'

In [2]: name
Out[2]: 'hui'

In [3]: age = 21

In [4]: age
Out[4]: 21
```

> 使用交互式方式，如果要查看变量内容，直接输入变量名即可，不需要使用 `print` 函数

<br/>

### 2）变量演练 2 —— PyCharm

```python
name = "hui"

age = 21

print(name)
print(age)
```

> 使用解释器执行，如果要输出变量的内容，必须要要使用 `print` 函数

<br/>

### 3）变量演练 3 —— 超市买猪肉

> - 可以用 **其他变量的计算结果** 来定义变量
> - 变量定义之后，后续就可以直接使用了

<br/>

**需求**

- 猪肉的价格是 **50 元 / 公斤**
- 买了 **1.5 公斤** 猪肉
- 计算付款金额

```python
# 定义猪肉价格变量
price = 50

# 定义购买重量 /kg
weight = 1.5

# 计算金额
money = price * weight

print(money)	# 75.0

# 老板太好了，给我们减了5元
money = money - 5
```

<br/>

**问答时刻 Question and Answer**

**`Q:`** 上述代码中，一共定义有几个变量？

**`A:`** 三个：`price`／`weight`／`money`

<br/>

**`Q:`** `money = money - 5` 是在定义新的变量还是在使用变量？

**`A:`**

- 变量名 只有在 **第一次出现** 才是 **定义变量**

- 变量名 再次出现，不是定义变量，而是直接使用之前定义过的变量

<br/>

**`Q:`** 在程序开发中，可以修改之前定义变量中保存的值吗？

**`A:`**

- 可以

- 变量中存储的值，就是可以 **变** 的

<br/>

## 二、 变量的类型

在内存中创建一个变量，会包括：

1. 变量的名称
2. 变量保存的数据
3. 变量存储数据的类型
4. 变量的地址

<br/>

### 1）变量类型的演练 —— 个人信息

**需求**

- 定义变量保存小汪的个人信息
- 姓名：**小汪**
- 年龄：**21** 岁
- 性别：**是**男生
- 身高：**1.63** 米
- 体重：**58** 公斤

<br/>

```python
In [16]: name = '小汪'

In [17]: age = 21

In [18]: sex = True

In [19]: height = 1.63

In [20]: weight = 58

In [21]: type(name)
Out[21]: str

In [22]: type(age)
Out[22]: int

In [23]: type(height)
Out[23]: float

In [24]: type(weight)
Out[24]: int
```

<br/>

> 利用 **`type()`** 函数可以确认变量中保存数据的类型

<br/>

**问答时刻**

**`Q:`** 在演练中，一共有几种数据类型？

**`A:`**

- 4 种
- `str` —— 字符串
- `bool` —— 布尔（真假）
- `int` —— 整数
- `float` —— 浮点数（小数）

<br/>

**`Q:`** 在 `Python` 中定义变量时需要指定类型吗？

**`A:`**

- 不需要
- `Python` 可以根据 `=` 等号右侧的值，自动推导出变量中存储数据的类型

<br/>

### 2）变量的类型

> 在 `Python` 中定义变量是 **不需要指定类型**（在其他很多高级语言中都需要）
>
> 数据类型可以分为 **数字型** 和 **非数字型**

<br/>

#### 数字型

- 整型 (`int`)
- 浮点型（`float`）
- 布尔型（`bool`） 
  - 真 `True`  —— **非零即真**
  - 假 `False` `0`
- 复数型 (`complex`)
  - 主要用于科学计算，例如：平面场问题、波动问题、电感电容等问题

<br/>

#### 非数字型

- 字符串
- 列表
- 元组
- 字典

<br/>

## 三、不同类型变量之间的计算

### 1）数字型变量之间可以直接计算

- 在 `Python` 中，两个数字型变量是可以直接进行**算数运算**
- 如果变量是 `bool` 型，在计算时
  - `True` 对应的数字是 `1`
  - `False` 对应的数字是 `0`

<br/>

**IPython 测验**

```python
In [31]: a = 10

In [32]: b = 3.14

In [33]: c = True

In [34]: d = False

In [35]: a + b
Out[35]: 13.14

In [36]: a + c
Out[36]: 11

In [37]: a + d
Out[37]: 10

In [38]: c + d
Out[38]: 1
```

<br/>

### 2）字符串变量之间使用 `+` 拼接字符串

> 在 Python 中，字符串之间可以使用 `+` 拼接生成新的字符串

```python
In [1]: first_name = "张"

In [2]: last_name = "三"

In [3]: first_name + last_name
Out[3]: '张三'
```

<br/>

### 3）字符串变量使用 `*` 重复拼接相同的字符串

```python
In [1]: "-" * 50
Out[1]: '--------------------------------------------------'
```

<br/>

### 4）数字型变量和字符串之间不能进行的计算

```python
In [40]: name = 'hui'

In [41]: age = 21

In [42]: name + age
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-42-977d5c2bd9b9> in <module>
----> 1 name + age

TypeError: can only concatenate str (not "int") to str
```

<br/>

> 类型错误：仅支持 str类型与str类型进行连接

<br/>

## 四、变量类型之间的转换

| 方法           | 描述                                 |
| -------------- | ------------------------------------ |
| **`int(x)`**   | 把 `x` 转换成 `int` 类型（整数）     |
| **`float(x)`** | 把 `x` 转换成 `float` 类型（浮点数） |
| **`str(x)`**   | 把 `x` 转换成 `str` 类型（字符串）   |

<br/>

### 1）转字符串 str

```python
In [61]: name = 'hui'

In [62]: age = 21

In [63]: sex = True

In [64]: height = 1.75

In [65]: type(name), type(age), type(sex), type(height)
Out[65]: (str, int, bool, float)

In [71]: name = str(name)

In [72]: age = str(age)

In [73]: sex = str(sex)

In [74]: height = str(height)

In [75]: name, age, sex, height
Out[75]: ('hui', '21', 'True', '1.75')

In [76]: type(name), type(age), type(sex), type(height)
Out[76]: (str, str, str, str)
```

<br/>

### 2）转整数 int

```python
In [86]: age = '21'

In [87]: height = 1.75

In [88]: sex = True

In [89]: int(age)
Out[89]: 21

In [90]: int(height)
Out[90]: 1

In [91]: int(sex)
Out[91]: 1

In [92]: flag = False

In [93]: int(flag)
Out[93]: 0

In [94]: name = 'hui'

In [95]: int(name)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-95-f75bcf899621> in <module>
----> 1 int(name)

ValueError: invalid literal for int() with base 10: 'hui'    
```

<br/>

> 浮点数转成 `int` 时都是 **向下取整**，例如：`int(3.14) -> 3, int(9.99) -> 9`
>
> 字符串只有是整数的形式才可以转成 `int`

<br/>

### 3）转浮点数 float

```python
In [97]: age = 21

In [98]: sex = True

In [99]: flag = False

In [100]: float(age)
Out[100]: 21.0

In [101]: float(sex)
Out[101]: 1.0

In [102]: float(flag)
Out[102]: 0.0

In [103]: name = 'hui'

In [104]: num = '3.14'

In [105]: float(num)
Out[105]: 3.14

In [106]: num = '10'

In [107]: float(num)
Out[107]: 10.0

In [108]: float(name)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-108-8e2822995b26> in <module>
----> 1 float(name)

ValueError: could not convert string to float: 'hui'
```

<br/>

> 要是数字形式的字符串，才可以转换成 `float` 浮点数型

<br/>

## 尾语

**✍ 用  Code 谱写世界，让生活更有趣。❤️**

**✍ 万水千山总是情，点赞再走行不行。❤️**

**✍ 码字不易，还望各位大侠多多支持。❤️**

<br/>

![010.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f3f0062e74c4b589e00414097f1a7cf~tplv-k3u1fbpfcp-watermark.image)