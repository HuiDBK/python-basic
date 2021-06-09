# Python 变量的命名规范

## 引言

> 混乱或错误的命名不仅让我们对代码难以理解，更糟糕的是，会误导我们的思维，导致对代码的理解完全错误。相反，良好的命名，则可以让我们的代码非常容易读懂，也能向读者正确表达事物以及逻辑的本质，从而使得代码的可维护性就大大增强，读命名好的文章是非常流畅的，会有一种享受的感觉。

<br/>

##  标识符和关键字

### 标识符

> 标识符就是程序员定义的 **变量名**、**函数名**
>
> **名字** 需要有 **见名知义** 的效果，见下图：

![见名知义](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb5ae47d217c49a8832d6716b413b2dc~tplv-k3u1fbpfcp-watermark.image)

- 标识符可以由 **字母**、**下划线** 和 **数字** 组成
- **不能以数字开头**
- 标识符对大小写敏感

<br/>

在 `Python 3` 中，可以用中文作为变量名，非 `ASCII` 标识符也是允许的了。

```python
In [1]: 名字 = 'hui'

In [2]: 性别 = '男'

In [3]: 名字 + 性别
Out[3]: 'hui男'
```

但一般不推荐使用中文来命名。

<br/>

### 关键字

- **关键字** 就是在 `Python` 内部已经使用的标识符
- **关键字** 具有特殊的功能和含义

通过以下命令可以查看 `Python` 中的关键字及数量

```python
In [110]: import keyword
    
In [111]: len(keyword.kwlist)
Out[111]: 35
    
In [112]: keyword.kwlist
Out[112]:
['False',
 'None',
 'True',
 'and',
 'as',
 'assert',
 
 ...篇幅太长故省略...
 
 'while',
 'with',
 'yield']

In [112]:
```

<br/>

> - `import` **xxx** 可以导入一个 **工具包/库**，在 `Python` 中不同的工具包/库，提供不同的功能
> - `len()` 函数通常用于**返回字符串、列表、字典、元组等长度**。

<br/>

> **定义变量、函数、类，千万不要与关键字重名**

```python
In [1]: book = 'Python 入门与实践'

In [3]: book
Out[3]: 'Python 入门与实践'

In [4]: type(book)
Out[4]: str

In [5]: type = '教育类型'

In [6]: type
Out[6]: '教育类型'

In [7]: type(book)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-5cf23ed0398b> in <module>
----> 1 type(book)

TypeError: 'str' object is not callable

In [8]:
```

<br/>

`type` 原是用来查看变量的数据类型的，但定义了一个与关键字 `type` 同名的变量，导致 `type` 函数的功能失效了，因此不要定义与关键字同名的变量。

<br/>

## 变量的命名规范

> **命名规范** 可以被视为一种 **惯例**，并无绝对与强制 目的是为了 **增加代码的识别和可读性**

<br/>

### 下划线命名法

1. 在定义变量时，为了保证代码格式，`=` 的左右应该各保留一个空格

2. 在 `Python` 中，如果 **变量名** 需要由 **二个** 或 **多个单词** 组成时，可以按照以下方式命名

   - 每个单词都使用小写字母

   - 单词与单词之间使用 **`_`下划线** 连接

   - 例如：`first_name`、`last_name`、`qq_number`、`qq_password`

<br/>

**注意** `Python` 中的 **标识符** 是 **区分大小写的**

![大小写敏感](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbca04b5d80e4f7588839312e995ecca~tplv-k3u1fbpfcp-watermark.image)

<br/>

### 驼峰命名法

- 当 **变量名** 是由二个或多个单词组成时，还可以利用驼峰命名法来命名
- **小驼峰式命名法**
  - 第一个单词以小写字母开始，后续单词的首字母大写
  - 例如：`firstName`、`lastName`
- **大驼峰式命名法**
  - 每一个单词的首字母都采用大写字母
  - 例如：`FirstName`、`LastName`、`CamelCase` 

![驼峰命名法](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/104fccf6247f4b7c8da839fd3e77df5d~tplv-k3u1fbpfcp-watermark.image)

<br/>

> `Java、C` 等其他语言一般用 **驼峰命名法**，在 `Python` 中则推荐使用**下划线命名法**，符合 `PEP8` 规范。

<br/>

## 尾语

**✍ 用  Code 谱写世界，让生活更有趣。❤️**

**✍ 万水千山总是情，点赞再走行不行。❤️**

**✍ 码字不易，还望各位大侠多多支持。❤️**

<br/>

![011.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/328dc211737241eebe549d1d6c5cd603~tplv-k3u1fbpfcp-watermark.image)