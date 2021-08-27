# Python 集合 — set

## 引言

> `set`（集合）虽然用的很少，但它是一个无序的不重复元素序列，用来简单的去重挺快的。

<br/>

## 集合的定义

> - `set`（集合） 与列表类似，不同之处在于集合的 **元素不重复**
> - 集合和字典一样也是用 `{}` 定义，但元素之间使用 `,` 分隔，或者使用 `set()`

<br/>

**`{ }` 定义**

```Python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

name_set = {'hui', 'wang', 'zack', 'hui'}

print(name_set)    	# 结果为 {'hui', 'wang', 'zack'}

name_set = set('hui', 'wang', 'zack', 'hui')

```

<br/>

**`set()` 定义**

> set() 只接受一个参数

```python
In [13]: name_set = set('hui')

In [14]: name_set
Out[14]: {'h', 'i', 'u'}

In [15]: name_set = set(['hui', 'wang', 'zack', 'hui'])

In [16]: name_set
Out[16]: {'hui', 'wang', 'zack'}
```

<br/>

**注意：空集合不能用 `s = {}` 来定义这样默认是字典，应该 `s = set()`**

```python
In [27]: s = {}

In [28]: s1 = set()

In [29]: type(s)
Out[29]: dict

In [30]: type(s1)
Out[30]: set
```

<br/>

## 集合常用操作

集合所有内置方法如下：

![集合内置方法](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a1846f9255c4f248f2388b84c96d770~tplv-k3u1fbpfcp-watermark.image)

方法太多我选几个常用的测试一下。

<br/>

### 集合添加元素

使用 `add()` 即可向集合中添加元素

```python
In [33]: s = set()

In [34]: s.add(1)

In [35]: s.add(4)

In [36]: s.add(3)

In [37]: s
Out[37]: {1, 3, 4}

In [38]: s.add(2)

In [39]: s
Out[39]: {1, 2, 3, 4}
```

<br/>

### 集合移除元素

- `remove()` 移除集合中的元素，且如果元素不存在，**会报错**
- `discard()` 移除集合中的元素，且如果元素不存在，**不会发生错误**
- `pop()` 随机移除集合内的一个元素

<br/>

```python
In [38]: # remove() 移除
In [39]: s
Out[39]: {1, 2, 3, 4}

In [40]: s.remove(3)

In [41]: s
Out[41]: {1, 2, 4}

In [42]: s.remove(5)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-42-9ec04578636f> in <module>
----> 1 s.remove(5)

KeyError: 5
```

<br/>

```python
In [45]: # discard() 移除

In [46]: s
Out[46]: {1, 2, 4}

In [47]: s.discard(4)

In [48]: s
Out[48]: {1, 2}

In [49]: s.discard(3)

In [50]: s
Out[50]: {1, 2}
```

<br/>

```python
In [56]: # pop() 随机移除

In [57]: s.pop()
Out[57]: 1

In [58]: s
Out[58]: {2, 3, 9, 'hui'}

In [59]: s.pop()
Out[59]: 2

In [60]: s
Out[60]: {3, 9, 'hui'}
```

<br/>

**其实`set` 集合的 `pop`方法会将集合的左边第一个元素进行删除，并返回删除的元素。**

<br/>

### 集合统计、清空元素

- `len()` 统计集合元素个数
- `clear()` 清空集合

<br/>

```python
In [68]: name_set
Out[68]: {'wang', 'zack'}

In [69]: len(name_set)
Out[69]: 2

In [71]: name_set.clear()

In [72]: len(name_set)
Out[72]: 0

In [73]: name_set
Out[73]: set()
```

<br>

### 集合元素获取(遍历)

> 集合不支持索引，也没有方法进行获取，因此只能采用 `for ... in ...` 遍历方式获取元素。

<br/>

```python

In [81]: name_set
Out[81]: {'hui', 'wang', 'zack'}

In [82]: for name in name_set:
    ...:     print(name)
    ...:
hui
wang
zack

In [83]: name_set[0]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-83-c0ead6d21f1d> in <module>
----> 1 name_set[0]

TypeError: 'set' object is not subscriptable
```

<br/>

## 集合之间的运算

### 集合差运算 `-`

```python
In [89]: a = {1, 2, 3, 4, 5}

In [90]: b = {1, 2, 3, 6}

In [91]: a - b
Out[91]: {4, 5}

In [92]: b - a
Out[92]: {6}
    
In [93]: a.difference(b)
Out[93]: {4, 5}

In [94]: b.difference(a)
Out[94]: {6} 
   
```

<br/>

- `a - b` 就相当于在 `a` 中去除跟 `b` 相同的元素
- `b - a` 也就是在 `b` 中去除跟 `a` 相同的元素
- `a - b` 等同于 `a.difference(b)`

<br/>

### 集合并运算 `|`

```python
In [95]: a
Out[95]: {1, 2, 3, 4, 5}

In [96]: b
Out[96]: {1, 2, 3, 6}

In [97]: a | b
Out[97]: {1, 2, 3, 4, 5, 6}
```

<br/>

### 集合交运算 `&`

```python
In [99]: a
Out[99]: {1, 2, 3, 4, 5}

In [100]: b
Out[100]: {1, 2, 3, 6}

In [101]: a & b
Out[101]: {1, 2, 3}
```

<br/>

### 集合异或运算 `^`

```python
In [102]: a
Out[102]: {1, 2, 3, 4, 5}

In [103]: b
Out[103]: {1, 2, 3, 6}

In [104]: a ^ b
Out[104]: {4, 5, 6}
```

把  `a, b` 集合中的相同元素都去掉，剩下的就是 `^` 异或运算的结果。

<br/>

## 应用场景

### 普通for循环去重

```python
In [1]: li = [2, 1, 3, 6, 2, 1]

In [2]: temp = []

In [3]: for i in li:
   ...:     if i not in temp:
   ...:         temp.append(i)
   ...:

In [4]: li
Out[4]: [2, 1, 3, 6, 2, 1]

In [5]: temp
Out[5]: [2, 1, 3, 6]
```

<br/>

### 利用集合简单去重

```python
In [106]: li = [1, 2, 2, 3, 3, 5]

In [107]: li = set(li)

In [108]: li
Out[108]: {1, 2, 3, 5}

In [109]: type(li)
Out[109]: set

In [110]:

```

这样把原来的列表类型变成了集合类型，这样更不好操作，这样不是想要的结果。

因此要做到 **去重加类型不变**，只要再嵌套一个`list()` 即可

```python
In [110]: li = [1, 2, 2, 3, 3, 5]

In [111]: li = list(set(li))

In [112]: li
Out[112]: [1, 2, 3, 5]

In [113]: type(li)
Out[113]: list

In [114]:

```

<br/>

### 去重保持原来的顺序

#### 使用 `sort + set` 去重

```python

In [6]: list1 = [2, 1, 3, 6, 2, 1]

In [7]: list2 = list(set(list1))

In [8]: list2
Out[8]: [1, 2, 3, 6]

In [9]: list2.sort(key=list1.index)

In [10]: list2
Out[10]: [2, 1, 3, 6]
```

 <br/>

#### 使用 `sorted + set` 去重

```python
In [12]: list1 = [2, 1, 3, 6, 2, 1]

In [13]: temp = sorted(set(list1), key=list1.index)

In [14]: temp
Out[14]: [2, 1, 3, 6]
```

<br/>

## 尾语

**✍ 用  Code 谱写世界，让生活更有趣。❤️**

**✍ 万水千山总是情，点赞再走行不行。❤️**

**✍ 码字不易，还望各位大侠多多支持。❤️**

![021.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a103eaf901143c48f584ecc124f3cf5~tplv-k3u1fbpfcp-watermark.image)
