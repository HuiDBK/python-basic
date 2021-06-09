# Python 条件控制 — `if`语句

## 引言

> 生活中的判断几乎是无所不在的，我们每天都在做各种各样的选择，如果这样？如果那样？……

<br/>

## 程序中的判断

### 流程判断示意图

```flow
st=>start: 开始
e=>end: 结束
op=>operation: 相关操作
cond=>condition: 条件

st->cond->op->e

cond(yes)->op
cond(no)->e
```

<br/>

### 成绩等级判断

- 60分以下为**不及格 D**
- 60 - 70 为**及格 C**
- 70 - 80 为**良好 B**
- 80 - 100 为**优秀 A**

<br/>

```flow
s=>start: 开始
e=>end: 结束

input_score=>operation: 输入分数
level_A=>operation: 优秀A
level_B=>operation: 良好B
level_C=>operation: 及格C
level_D=>operation: 不及格D

D=>condition: 分数 < 60
C=>condition: 60 <= 分数 < 70
B=>condition: 70 <= 分数 < 80
A=>condition: 80 <= 分数 <= 100

s->input_score->D->C->B->A->e

D(yes)->level_D->e
D(no)->C(yes)->level_C->e
C(no)->B(yes)->level_B->e
B(no)->A(yes)->level_A->e
```

<br/>

流程图可以非常直观地描述一个工作过程。

<br/>

## Python中的 `if` 语句

### if 语句基本语法

在 `Python` 中，**if 语句** 就是用来进行判断的，格式如下：

```python
if 要判断的条件:
    条件成立时，要做的事情
    ...
```

<br/>

```python
if 要判断的条件:
    条件成立时，要做的事情
    ...
else:
    条件不成立，要做的事情
```

<br/>

```python
if 要判断的条件:
    条件成立时，要做的事情
    ...
elif 要判断的条件:
    条件成立，要做的事情
    ...
elif 要判断的条件:
    条件成立，要做的事情
    ...
else:
    所有条件都不成立时，要做的事情
```

<br/>

**注意：**

- 每个条件后面要使用**冒号 `:`**，表示接下来是满足条件后要执行的语句块。
- 使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
- `Python` 中代码的缩进为一个 `tab` 键，或者 **4** 个空格 —— **建议使用空格** 符合 `PEP8` 规范。

> `PyCharm` 中使用 `tab` 键缩进会自动转换成 `4` 个空格。

<br/>

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

**陪女朋友过节**

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 节日名称
holiday_name = "平安夜"

if holiday_name == "情人节":
    print("买玫瑰")
    print("看电影")
elif holiday_name == "平安夜":
    print("买苹果")
    print("吃大餐")
elif holiday_name == "生日":
    print("买蛋糕")
else:
    print("每天都是节日啊……")
```

<br/>

**成绩等级判断**

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

其中 

- `elif score < 70:` 相当于 `if score >= 60 and score <70`
- `elif score < 80:` 相当于 `if score >= 70 and score <80`
- 。。。

当 `score` 分数为 `85` 分时，

- `if score < 60` 条件不满足，说明分数 `>60` 走 `elif`
- `score < 70` 条件还是不满足，说明分数 `>70` 继续走 `elif`
- `score < 80` 条件不满足，说明分数 `>80` 继续走 `elif`
- `score < 90` **条件满足**，输出 **良好** 

<br/>

> `if ... elif...` 的应用场景是：**同时** 判断 **多个条件**，所有的条件是 **平级** 的

<br/>

### 多条件 if 判断

> 利用 **逻辑运算符 `and, or, not`**，来进行多个条件判断

**`and` 测验**

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

python_score = 85	# python 分数
c_score = 80		# c语言 分数

# 要求两门成绩 >= 60 分就算合格
if python_score >= 60 and c_score >= 60:
    print("考试通过")
else:
    print("再接再厉！")
```

<br/>

**`or` 测验**

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

user = '管理员'

if user == '管理员' or user == '超级管理员':
	print('欢迎!')
else:
    print('没有权限')
```

<br/>

**`not` 测验**

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 员工标识
is_employee = True

# 如果不是本公司员工
if not is_employee:
    print("非本公司员工不允许入内")
```

<br/>

### if 嵌套

> **if 的嵌套** 就是：**在之前条件满足的前提下，再增加额外的判断**

<br/>

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

ranking = 2	# 排名
gender = '男'

# 前三名进入决赛
if ranking <= 3:
    print('进入决赛')
 
    if gender == '男':
        print('进入男子组')
    elif gender == '女':
        print('进入女子组')
else:
	print('重在参与！')
```

<br/>

## 实战案例

### 随机数的处理

> 下面案例中都使用到了随机数，因此先介绍一下在 `Python` 如何生成一个随机数。

- 在 `Python` 中，要使用随机数，首先需要导入 **随机数** 的 **模块** —— “工具包”

```python
import random
```

- `random.randint(a, b)` ，返回 `[a, b]` 之间的整数，包含 `a` 和 `b`
- `random.random()` ，返回  `[0, 1)` 之间的浮点数，不包含 `1`

<br/>

```python
In [1]: import random

In [2]: random.random()
Out[2]: 0.2996451389925341

In [3]: random.random()
Out[3]: 0.9148908780729963

In [4]: random.random()
Out[4]: 0.9864410356222624
    
In [9]: random.randint(1, 10)
Out[9]: 1

In [10]: random.randint(1, 10)
Out[10]: 9

In [11]: random.randint(1, 10)
Out[11]: 5

In [12]: random.randint(1, 10)
Out[12]: 6
```

<br/>

> 注意 `random.randint(20, 10)`  这样的语句是错误的，**下限必须小于上限**

<br/>

### 石头剪刀布

**需求**

1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
2. 电脑 **随机** 出拳，比较胜负

| 序号 |     规则     |
| :--: | :----------: |
|  1   | 石头 胜 剪刀 |
|  2   |  剪刀 胜 布  |
|  3   |  布 胜 石头  |

<br/>

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 石头剪刀布小案例 }
# @Date: 2021/06/09 22:16
import random

player = input('请出拳 石头（1）／剪刀（2）／布（3）: ')

player = int(player)

computer = random.randint(1, 3)

if (player == 1 and computer == 2) or \
        (player == 2 and computer == 3) or \
        (player == 3 and computer == 1):

    print('玩家赢了，电脑弱爆了！！！')
elif player == computer:
    print('心有灵犀一点通，平局')
else:
    print('电脑赢了, 不行我要和你决战到天亮')
```

<br/>

![石头剪刀布运行结果](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ab20405a95c4827a8ed2d934848c04d~tplv-k3u1fbpfcp-watermark.image)

<br/>

> 注意 `input()` 返回的是字符串，记得转换成 `int` 

<br/>

## 尾语

**✍ 用  Code 谱写世界，让生活更有趣。❤️**

**✍ 万水千山总是情，点赞再走行不行。❤️**

**✍ 码字不易，还望各位大侠多多支持。❤️**

<br/>

![012.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0e9be5fc51e459eb2ea301ad36d1d85~tplv-k3u1fbpfcp-watermark.image)