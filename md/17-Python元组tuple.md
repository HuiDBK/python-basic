# Python 元组 — tuple

##  元组的定义

- `Tuple`（元组）与列表类似，不同之处在于元组的 **元素不能修改**
  - **元组** 表示多个元素组成的序列
  - **元组** 在 `Python` 开发中，有特定的应用场景
- 用于存储 **一串 信息**，**数据** 之间使用 `,` 分隔
- 元组用 `()` 定义
- 元组的 **索引** 从 `0` 开始
  - **索引** 就是数据在 **元组** 中的位置编号

```python
info_tuple = ("hui", 21, 1.75)
```

 <br/>

### 创建元组

```python
info_tuple = ()    # 空元组
```

<br/>

元组中 **只包含一个元素** 时，需要 **在元素后面添加逗号**

```
info_tuple = (21, )
```

如果不添加逗号的话，将不是元组类型，用 `IPython` 进行测验一下：

```python
In [1]: info_tuple = (50)

In [2]: info_tuple
Out[2]: 50

In [3]: type(info_tuple)
Out[3]: int

In [4]: info_tuple = (50, )

In [5]: type(info_tuple)
Out[5]: tuple

In [6]: info_tuple
Out[6]: (50,)

In [7]:
```

经测验发现，不添加逗号的话，类型为 `int` 不是元组。

> 因此当创建一个只有一个元素的元组时，需要 **在元素后面添加逗号**
>
> - info_tuple = (21,  )     √    类型是元组
> - info_tuple = (21)        X     类型不是元组，是整型

<br/>

### 元组元素不可修改

```python

In [69]: info_tuple = ('hui', 21, 1.75)

In [70]: info_tuple[0]
Out[70]: 'hui'

In [71]: info_tuple[0] = 'wang'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-71-40015c5375d3> in <module>
----> 1 info_tuple[0] = 'wang'

TypeError: 'tuple' object does not support item assignment
```

类型错误：元组对象不支持元素的赋值操作

<br/>

## 元组常用操作

> 元组中方法很少就两个
>
> - index()   获取元素第一次在元组中出现的索引
> - count()  统计元素在元组中出现的次数

![元组常用操作](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f801a24ca76142f28fd3e719f6c44b73~tplv-k3u1fbpfcp-watermark.image)

 <br/>

- 在 `ipython` 中定义一个 **元组**，例如：`info_tuple = (50, )`
- 输入 `info_tuple.` 按下 `TAB` 键，`ipython` 会提示 **元组** 能够使用的函数如下：

![元组的方法](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e8bb3e23efc4211a94f833eee12256e~tplv-k3u1fbpfcp-watermark.image)

 <br/>

### 元组index()方法测验

> `index()` 方法的作用：获取元素第一次在元组中出现的索引

```python
In [8]: info_tuple = ('hui', 'zack', 'wang', 'hui')

In [9]: info_tuple.index('hui')
Out[9]: 0

In [10]: info_tuple.index('zack')
Out[10]: 1

In [11]: info_tuple.index('wang')
Out[11]: 2
```

<br/>

### 元组count()方法测验

> count() 方法的作用：统计元素在元组中出现的次数

```python
In [12]: info_tuple = ('hui', 'zack', 'wang', 'hui')

In [13]: info_tuple.count('hui')
Out[13]: 2

In [14]: info_tuple.count('zack')
Out[14]: 1

In [15]: info_tuple.count('wang')
Out[15]: 1
```

<br/>

## 循环遍历

- **取值** 就是从 **元组** 中获取存储在指定位置的数据
- **遍历** 就是 **从头到尾** **依次** 从 **元组** 中获取数据

```python
In [17]: info_tuple = ('hui', 21, 1.75)

In [18]: for obj in info_tuple:
    ...:     print(obj)
    ...:
hui
21
1.75

In [19]:


```

> 在 `Python` 中，可以使用 `for` 循环遍历所有非数字型类型的变量：**列表**、**元组**、**字典** 以及 **字符串**
>
> 在实际开发中，除非 **能够确认元组中的数据类型**，否则针对元组的循环遍历需求并不是很多

 <br/>

## 应用场景

### 互换两个变量值

通常情况我们要借助一个临时变量来辅助进行互换连个变量的值

```python
In [23]: a = 10

In [24]: b = 20

In [25]: # 借助临时变量的情况

In [26]: temp = a

In [27]: a = b

In [28]: b = temp

In [29]: a
Out[29]: 20

In [30]: b
Out[30]: 10

```

<br/>

而在Python中可以借助元组非常的便捷的来完成互换变量值。

```python
In [31]: # 利用元组

In [32]: a = 10

In [33]: b = 20

In [34]: a, b = b, a

In [35]: a
Out[35]: 20

In [36]: b
Out[36]: 10
```

<br/>

### 当做函数的参数和返回值

一个函数可以接收 **任意多个参数**，或者 **一次返回多个数据**

**函数返回多个数据**

```python
In [45]: def get_info():
    ...:     name = 'hui'
    ...:     age = 21
    ...:     return name, age
    ...:

In [46]: name, age = get_info()

In [47]: name
Out[47]: 'hui'

In [48]: age
Out[48]: 21

In [49]: type(get_info())
Out[49]: tuple
```

<br/>

通过上面代码可以看出，函数返回的结果类型为**元组**

**`Q:`** 为什么返回的是元组类型呢？

**`A:`** 首先 **Python解释器** 会将 `name，age` 变量进行装包，打包成一个整体即**元组**，但返回格式的变量之间必须要有逗号隔开。所以返回的类型是元组，达到了函数返回多个数据的功能。

<br/>

**`Q:`** 返回的竟然是元组类型，接收函数返回结果又怎么能用多个变量呢？

**`A:`** 返回可以将多个变量打包成元组，那么解释器也可以将元组拆包成多个变量

这是Python解释器隐式帮我们完成了**元组的装、拆包的过程**。

<br/>

**函数接受任意参数**

```python
In [54]: def set_info(*args):
    ...:     print(type(args))
    ...:     print(args)
    ...:

In [55]: set_info('hui', 21)
<class 'tuple'>
('hui', 21)

In [56]:
```

将非关键字参数打包成元组进行参数窗体，具体细节将在后面的函数进阶会详细讲解，这里先了解一下。

<br/>

**格式字符串**

格式化字符串后面的 `()` 本质上就是一个元组

```python
In [38]: name = 'hui'

In [39]: age = 21

In [40]: info = (name, age)

In [41]: type(info)
Out[41]: tuple

In [43]: print('%s 的年龄为 %d' % (name, age))
hui 的年龄为 21

In [44]: print('%s 的年龄为 %d' % info)
hui 的年龄为 21

In [45]:
```

<br/>

### 元组和列表之间的转换

**让列表变成成元组元素不可以被修改**，以保护数据安全

使用 `list` 函数可以把元组转换成列表

```python
In [63]: infos = ('hui', 21, 1.75)

In [64]: type(infos)
Out[64]: tuple

In [65]: infos
Out[65]: ('hui', 21, 1.75)

In [66]: infos = list(infos)

In [67]: type(infos)
Out[67]: list

In [68]: infos
Out[68]: ['hui', 21, 1.75]
```

<br/>

使用 `tuple` 函数可以把列表转换成元组

```python
In [72]: infos = [1, 2, 3, 4, 5]

In [73]: type(infos)
Out[73]: list

In [74]: infos
Out[74]: [1, 2, 3, 4, 5]

In [75]: infos = tuple(infos)

In [76]: type(infos)
Out[76]: tuple

In [77]: infos
Out[77]: (1, 2, 3, 4, 5)
```

 <br/>

## 尾语

**✍ 用  Code 谱写世界，让生活更有趣。❤️**

**✍ 万水千山总是情，点赞再走行不行。❤️**

**✍ 码字不易，还望各位大侠多多支持。❤️**

<br/>

![017.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b21d4968a0604db3b80e4d4b104240d5~tplv-k3u1fbpfcp-watermark.image)