# Python 列表 — list

## 引言

> `list`（列表） 是 `Python` 中使用 **最频繁** 的数据类型，在其他语言中通常叫做 **数组**

<br/>

## 列表定义

- 专门用于存储 **一组 信息**
- 列表用 `[]` 定义，**数据** 之间使用 `,` 分隔
- 列表的 **索引** 从 `0` 开始
  - **索引** 就是数据在 **列表** 中的位置编号，**索引** 又可以被称为 **下标**

<br/>

```python
name_list = ["hui", "zack", "wang"]
```

<br/>

![列表索引](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b509717216c4e5bac2da6dfa1830e64~tplv-k3u1fbpfcp-watermark.image)

 <br/>

> 注意：从列表中取值时，如果 **超出索引范围**，程序会报错

<br/>

## 列表常用操作

- 在 `IPython` 中定义一个 **列表**，例如：`name_list = []`
- 输入 `name_list.` 按下 `TAB` 键，`Ipython` 会提示 **列表** 能够使用的 **方法** 如下：

![列表方法提示](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c81370042ff4f508706e52640cabb05~tplv-k3u1fbpfcp-watermark.image)

<br/>

### 列表方法说明

| 序号 | 分类 | 方法                        | 说明                     |
| ---- | ---- | --------------------------- | ------------------------ |
| 1    | 增加 | **列表.insert(索引, 数据)** | 在指定位置插入数据       |
|      |      | **列表.append(数据)**       | 在末尾追加数据           |
|      |      | **列表.extend(列表2)**      | 将列表2 的数据追加到列表 |
| 2    | 修改 | **列表[索引] = 数据**       | 修改指定索引的数据       |
| 3    | 删除 | **del 列表[索引]**          | 删除指定索引的数据       |
|      |      | **列表.remove[数据]**       | 删除第一个出现的指定数据 |
|      |      | **列表.pop()**              | 删除末尾数据             |
|      |      | **列表.pop(索引)**          | 删除指定索引数据         |
|      |      | **列表.clear()**            | 清空列表                 |
| 4    | 统计 | **len(列表)**               | 列表长度                 |
|      |      | **列表.count(数据)**        | 数据在列表中出现的次数   |
| 5    | 排序 | **列表.sort()**             | 升序排序                 |
|      |      | **列表.sort(reverse=True)** | 降序排序                 |
|      |      | **列表.reverse()**          | 逆序、反转               |

 <br/>

### 列表增加数据 - IPython 测验

```python
In [2]: animal_list = ['牛', '虎', '兔']

In [3]: animal_list
Out[3]: ['牛', '虎', '兔']

In [4]: # insert 指定位置插入数据

In [5]: animal_list.insert(0, '鼠')  # 往列表第 0 位置插入

In [6]: animal_list
Out[6]: ['鼠', '牛', '虎', '兔']


In [7]: # append 在末尾追加数据

In [8]: animal_list.append('龙')

In [9]: animal_list
Out[9]: ['鼠', '牛', '虎', '兔', '龙']
    

In [10]: animal_list2 = ['蛇', '马', '羊']

In [11]: # expend 把其他列表数据追加到列表中

In [12]: animal_list.extend(animal_list2)

In [13]: animal_list
Out[13]: ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊']
    
```

<br/>

### 列表修改数据 - IPython 测验


```python
In [15]: name_list = ['hui', 'zhangsan', 'lisi']

In [16]: # 通过列表索引修改数据

In [17]: name_list[1] = 'zack'

In [18]: name_list
Out[18]: ['hui', 'zack', 'lisi']

In [19]: name_list[2] = 'wang'

In [20]: name_list
Out[20]: ['hui', 'zack', 'wang']

In [21]:
```

<br/>

### 列表删除数据 - IPython 测验

```python
In [21]: lang_list = ['python', 'java', 'c', 'c++', 'php']

In [22]: # del 关键字删除列表数据

In [23]: del lang_list[0]

In [24]: lang_list
Out[24]: ['java', 'c', 'c++', 'php']


In [25]: # remove 方法移除列表数据

In [26]: lang_list.remove('java')

In [27]: lang_list
Out[27]: ['c', 'c++', 'php']


In [28]: # pop 方法删除列表末尾数据

In [29]: lang_list.pop()
Out[29]: 'php'

In [30]: lang_list
Out[30]: ['c', 'c++']


In [31]: # pop 删除列表指定索引数据

In [32]: lang_list.pop(1)
Out[32]: 'c++'

In [33]: lang_list
Out[33]: ['c']


In [34]: # clear 方法清空列表

In [35]: lang_list.clear()

In [36]: lang_list
Out[36]: []

In [37]: name_list = ['hui', 'zack', 'wang']

In [38]: name_list.clear()

In [39]: name_list
Out[39]: []

```

<br/>

### 列表统计数据 - IPython 测验

```python
In [41]: name_list = ['hui', 'wang', 'zack', 'hui', 'hui', 'wang']

In [42]: # len 方法计算列表长度

In [43]: len(name_list)
Out[43]: 6

    
In [44]: # count 方法统计数据在列表中出现的次数

In [45]: name_list.count('hui')
Out[45]: 3

In [46]: name_list.count('wang')
Out[46]: 2

In [47]: name_list.count('zack')
Out[47]: 1
```

<br/>

### 列表数据排序 - IPython 测验

```python
In [49]: num_list = [2, 5, 3, 1, 6, 4, 7, 8]

In [50]: # sort 方法默认升序排序

In [51]: num_list.sort()

In [52]: num_list
Out[52]: [1, 2, 3, 4, 5, 6, 7, 8]
    

In [53]: # sort(reverse=True) 降序排序

In [54]: num_list.sort(reverse=True)

In [55]: num_list
Out[55]: [8, 7, 6, 5, 4, 3, 2, 1]
    

In [56]: # reverse 方法逆序、反转

In [57]: num_list.reverse()

In [58]: num_list
Out[58]: [1, 2, 3, 4, 5, 6, 7, 8]

In [59]: name_list = ['hui', 'wang', 'zack']

In [60]: name_list.reverse()

In [61]: name_list
Out[61]: ['zack', 'wang', 'hui']

In [62]:
```

<br/>

## 循环遍历列表

> **遍历** 就是 **从头到尾** **依次** 从 **列表** 中获取数据

<br/>

### while 循环遍历

```python
In [62]: name_list = ['hui', 'zack', 'wang']

In [63]: i = 0

In [64]: while i < len(name_list):
    ...:     print(name_list[i])
    ...:     i = i + 1
    ...:
hui
zack
wang
```

<br/>

> `while` 循环要判断列表的长度，然后通过列表索引获取数据

<br/>

### for 循环遍历

- 在 `Python` 中为了提高列表的遍历效率，专门提供的 **迭代 iteration 遍历**
- 使用 `for` 就能够实现迭代遍历

```python
In [62]: name_list = ['hui', 'zack', 'wang']
    
In [65]: for name in name_list:
    ...:     print(name)
    ...:
hui
zack
wang

```

<br>

**`Q:`** `for` 循环怎么才能知道遍历到哪个位置了？

**`A:`** 可以通过一个 计数器变量 `count`  来统计

```python
In [66]: name_list = ['hui', 'zack', 'wang']

In [67]: count = 0

In [68]: for name in name_list:
    ...:     print(count)
    ...:     print(name)
    ...:     count = count + 1
    ...:
0
hui
1
zack
2
wang
```

<br/>

**`A:`** 也可以通过内置函数 `enumerate()` 来进行枚举

```python
In [69]: name_list = ['hui', 'zack', 'wang']

In [70]: for i, name in enumerate(name_list):
    ...:     print(i)
    ...:     print(name)
    ...:
0
hui
1
zack
2
wang
```

<br/>

## 知识扩展

### del 关键字介绍

- 使用 `del` 关键字(`delete`) 同样可以删除列表中元素
- `del` 关键字本质上是用来 **将一个变量从内存中删除的**
- 如果使用 `del` 关键字将变量从内存中删除，后续的代码就不能再使用这个变量了

```python
name_list = ['hui', 'wang', 'zack']
del name_list[1]

# 删除整列表
del name_list
```

<br/>

> 在日常开发中，要从列表删除数据，建议 **使用列表提供的方法**

 <br/>

### 关键字、函数和方法

**关键字** 是 `Python` 内置的、具有特殊意义的标识符

```python
In [1]: import keyword
In [2]: print(keyword.kwlist)
In [3]: print(len(keyword.kwlist))
```

> 关键字后面不需要使用括号

<br/>

**函数** 封装了独立功能，可以直接调用

```python
def say_hello():
    print('hello')
    
say_hello()

```

> 函数需要死记硬背

<br/>

**方法** 和函数类似，同样是封装了独立的功能

**方法** 需要通过 **对象** 来调用，表示针对这个 **对象** 要做的操作

```python
name_list = ['hui', 'zack', 'wang']

name_list.sort()
name_list.reverse()
name_list.pop()
name_list.clear()
```

> 在对象后面输入 `.`，然后选择针对这个对象要执行的操作，记忆起来比函数要简单很多

 <br/>

## 尾语

**✍ 用  Code 谱写世界，让生活更有趣。❤️**

**✍ 万水千山总是情，点赞再走行不行。❤️**

**✍ 码字不易，还望各位大侠多多支持。❤️**

<br/>

![016.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11b909e194ca4653950c7e0f646d0878~tplv-k3u1fbpfcp-watermark.image)