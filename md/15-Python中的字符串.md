# Python 中的字符串

## 前言
> 现实生活中文字随处可见，编程语言中则用字符串来表示，字符串是Python中最常用的数据类型。想想在没有图形化界面的时代，几乎都是对字符串和数字的处理，衍生到后来的网页、Windows应用程序等都能看到对字符串的操作。还有每个国家都有不同的语言，而字符串有不同的字符串编码来表示。越容易小瞧的反而越重要

<br/>

## 英语词汇表

| 单词            | 中文解释                              |                全 称                 |
| :-------------- | :------------------------------------ | :----------------------------------: |
| **`UTF-8`**     | 针对 `Unicode` 的一种可变长度字符编码 | Unicode Transformation Format(8位元) |
| **`builtins`**  | 内置模块                              |                  \                   |
| **`format`**    | 格式、使格式化                        |                  \                   |
| **`separator`** | 分割符                                |                  \                   |
| **`suffix`**    | 后缀                                  |                  \                   |

<br/>

## 一、字符串编码

由于 Python 源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为<font color='#FF0059'> UTF-­8 编码</font>。当 Python 解释器读取源代码时，为了让它按 UTF-­8 编码读取，我们通常在文件开头写上这两行： 

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-
```

第一行注释是为了告诉 <font color='#FF0059'>Linux/OS X 系统，这是一个 Python 可执行程序</font>，Windows 系统会忽略这个注释； 

第二行注释是为了告诉<font color='#FF0059'> Python 解释器，按照 UTF­-8 编码读取源代码</font>，否则，你在源代码中写的中文输出可能会有乱码。我个人建议在每个Python文件中都写上这两行。

<br/>

## 二、字符串简单的使用

### 2.1 用print()打印字符串。

在 `Python` 中可以通过 **英文** 的  (双引号 **`"`**)  或者  (单引号 **`'`**)  识别出字符串来

```python
#!\usr\bin\python3
# -*- coding:utf-8 -*- 

content1 = 'hello world --- Python'
content2 = "hello world --- Java"

print(content1)
print(content2)

```

<br/>

### 2.2 在字符中显示(双引号 `"` )  或者  (单引号 `'` ) 

   #### 	单、双引号一起用

```python
#!\usr\bin\python3
# -*- coding:utf-8 -*- 

content3 = "Let's go"
content4 = '小明同学打乒乓球把玻璃给弄碎了，他是真的"很厉害"'
	
print(content3)
print(content4)
```
<br/>

   #### 	使用转义字符  `\`

``` python
#!\usr\bin\python3
# -*- coding:utf-8 -*- 

content5 = "C、Html、JavaScript、Css、\"Python\"、Java、Markdown"
content6 = 'My name is \'Hui\'!'

print(content5)
print(content6)
```

<br/>

**运行结果：**

```python
C、Html、JavaScript、Css、\"Python\"、Java、Markdown

My name is 'Hui'!
```

<br/>

### 2.3 中文的(单引号<font color='#FF059' size='5em'>‘</font>)、(双引号<font color='#FF0059' size='5em'>“</font>) 

然而在我们 **博大精深的中华文化** 当中， (单引号 **`‘`**)、(双引号**`“`**)  可以表示

1. **引号可表示引用**
2. **表示特定称谓**
3. **表示特殊含义**
4. **表示讽刺和嘲笑以及突出强调**

<br/>

```python 
content7 = "“怕什么！海的美就在这里！”我说道"
content8 = '现代画家徐悲鸿笔下的马，正如有的评论家所说的那样，“形神兼备，充满生机”。'
content9 = "他们（指友邦人士）维持他们的“秩序”的监狱，就撕掉了他们的“文明”的面具。"

print(content7)
print(content8)
print(content9)
```

<br/>

> 注意：在字符串中使用中文的(单引号 **`‘`**)、(双引号 **`“`** )不需要用转义字符 **`\`**

<br/>

### 2.4 运算符操作字符串

```python
#!\usr\bin\python3
# -*- coding:utf-8 -*- 

# 运算符操作字符串
print('5' + '3')    # --> '53'	拼接
print('--' * 20 + '分割线' + '--' * 20)	# '--' * 20 等同于20个'--'相加拼接

# 字符串累加
result = ''
for i in range(10):
    result += str(i)
print(result)   # -->'0123456789'
```

<br/>

## 三、字符串格式化

在 `Python` 中，采用的格式化方式和 **C 语言**是一致的，用 **`%`** 实现，如下：

| 格式             | 含义                                                 |
| ---------------- | ---------------------------------------------------- |
| **`%c`**         | 单字符 (整数 `ASCII` 值或者长度为 `1` 的字符)        |
| **`%r`**         | 字符串 (通过 `repr()` 进行转换)                      |
| **`%s`**         | 字符串 (通过 `str()` 进行转换)                       |
| **`%d` 或 `%i`** | 整型占位符                                           |
| **`%u`**         | 无符号的十进制整数                                   |
| **`%o`**         | 无符号的八进制整数                                   |
| **`%x` 或 `%X`** | 无符号的十六进制整数                                 |
| **`%e` 或 `%E`** | 指数符号(科学计数法)                                 |
| **`%f` 或 `%F`** | 浮点数(默认6位小数，四舍五入)                        |
| **`%g` 或 `%G`** | 如果指数大于-4或者小于-4精度值则和%e、%E、%f、%F相同 |

<br/>

你可能猜到了，`%` 运算符就是用来格式化字符串的。在字符串内部，`%s` 表示用字符串替换， `%d` 表示用整数替换，有几个 `%?` 占位符，后面就跟几个变量或者值，顺序要对应好。如果只 有一个 `%?`，括号可以省略。 常见的占位符有： `%d`  整数、` %f ` 浮点数 、`%s` 字符串、 `%x` 十六进制整数。

<br/>

**IPython 测验**

```python
In [7]: # %c 测验

In [8]: 'a%cc' % 'b'
Out[8]: 'abc'

In [9]: 'a%cc%c' % ('b', 'd')
Out[9]: 'abcd'

In [10]: 'a%cc%c' % ('b', 100)
Out[10]: 'abcd'
    
In [11]: # %r 测验

IIn [12]: 'a%rc' % 'b'
Out[12]: "a'b'c"

In [13]: 'a%rc%r' % ('b', 5)
Out[13]: "a'b'c5"

In [14]: # %s 测验

IIn [15]: 'a%sc' % 'b'
Out[15]: 'abc'

In [16]: 'a%sc%s' % ('b', 10)
Out[16]: 'abc10'

In [17]: 'a%sc%s' % ('b', 3.14)
Out[17]: 'abc3.14'

In [18]: 'a%sc%s' % ('b', '中文')
Out[18]: 'abc中文'    
    
# 整数测试    
In [19]: 'num=%d' % 150
Out[19]: 'num=150'

In [20]: 'num=%f' % 3.14
Out[20]: 'num=3.140000'

In [21]: 'num=%d' % 3.14
Out[21]: 'num=3'

In [22]: 'num=%i' % 100
Out[22]: 'num=100'

In [23]: 'num=%u' % 100
Out[23]: 'num=100'

In [24]: 'num=%o' % 100
Out[24]: 'num=144'

In [25]: 'num=%x' % 100
Out[25]: 'num=64'

In [26]: 'num=%e' % 100
Out[26]: 'num=1.000000e+02'

In [27]: 'num=%g' % 100
Out[27]: 'num=100'    
```

<br/>

> `%r` 是完全替换字符串不管转义符号、引号，要替换的东西长什么样，就原样替换成。
>
> 如果你不太确定应该用什么，`%s` 永远起作用，它会把任何数据类型转换为字符串

<br/>

其中，格式化整数和浮点数还可以指定是否补 `0` 和 指定小数的位数。

```python
In [32]: 'num=%03d' % 1
Out[32]: 'num=001'

In [33]: 'num=%03d' % 2
Out[33]: 'num=002'

In [34]: 'num=%03d' % 10
Out[34]: 'num=010'

In [35]: 'num=%03d' % 100
Out[35]: 'num=100'

In [36]: 'num=%.2f' % 3.1415926
Out[36]: 'num=3.14'

In [37]: 'num=%.6f' % 3.1415926
Out[37]: 'num=3.141593'
    
In [38]: '%05.2f' % 3.1415
Out[38]: '03.14'
```

<br/>

- 在 `%03d` 中的 `3` 代表字符串长度不足 `3` 自动向前补 `0`，直到字符串长度为 `3` 停止
- 在 `%05.2f` 中的 `5` 代表字符串长度不足 `5` 自动向前补 `0`，直到字符串长度为 `5`  停止， `2` 代表保留小数点后两位小数，最后一位四舍五入。`3.1415` 先是保留两位小数为 `3.14`，然后长度为 `4`，向前补 `0`

<br/>

### 模板字符串

> 在字符串最前面加上 `f` ，就是 **模板字符串**。
>
> 在 **模板字符串** 里面可以直接使用`{xxx}` 来引用变量或进行相应的运算。

<br/>

**IPython 测验**

```python
In [4]: a = 10

In [5]: b = 20

In [6]: f'num1={a}, num2={b}'
Out[6]: 'num1=10, num2=20'

In [7]: f'num1={a}, num2={b}, num3={a * b}'
Out[7]: 'num1=10, num2=20, num3=200'

In [8]: lang = 'Python'

In [10]: f'language is {lang}, length={len(lang)}'
Out[10]: 'language is Python, length=6'

In [11]:
```

<br/>

## 四、字符串的方法

> 由于字符串在编程中经常用到，因此 `Python` 对字符串的操作有非常多的方法。

<br/>

### 4.1 `dir()`查看 `str` 的所有方法

我们可以用内置模块( `builtins.py`) 的 `dir()` 来查看某个的类的所有方法，返回的是所有方法汇总的**列表(list)** 

<br/>

**打印字符串中的所有方法**

```Python
def out_demo_title(title):
    """
    打印案例标题
    :param title
    :return:
    """
    title = " " * 40 + title + " " * 40
    print("-" * 100)
    print(title)
    print("-" * 100)
    
    
def iter_out(iter_obj, row_num, left_just=18):
    """
    指定格式迭代输出
    :param iter_obj: 待输出的可迭代对象
    :param row_num: 一行输出多少个
    :param left_just: 左对齐的宽度
    :return:
    """
    for index in range(len(iter_obj)):
        print(iter_obj[index].ljust(left_just), end='')
        if (index+1) % row_num == 0:
            print()
            print('\n')


def main():
    content = 'Hello World --- Python'
    print(content)

    # 查看字符串类的所有方法
    print(dir(str))

    # 在一行上看不全且看的累，我们微调一下
    title = 'str类的所有方法(%d)' % len(dir(str))
    out_demo_title(title)
    iter_out(dir(str), row_num=5)
  	

main()

```

<br/>

**字符串所有方法如下：**

```text
-----------------------------------------------------------------------------------------------
                                        str类的所有方法(78)
-----------------------------------------------------------------------------------------------
__add__           __class__         __contains__      __delattr__       __dir__


__doc__           __eq__            __format__        __ge__            __getattribute__


__getitem__       __getnewargs__    __gt__            __hash__          __init__


__init_subclass__ __iter__          __le__            __len__           __lt__


__mod__           __mul__           __ne__            __new__           __reduce__


__reduce_ex__     __repr__          __rmod__          __rmul__          __setattr__


__sizeof__        __str__           __subclasshook__  capitalize        casefold


center            count             encode            endswith          expandtabs


find              format            format_map        index             isalnum


isalpha           isascii           isdecimal         isdigit           isidentifier


islower           isnumeric         isprintable       isspace           istitle


isupper           join              ljust             lower             lstrip


maketrans         partition         replace           rfind             rindex


rjust             rpartition        rsplit            rstrip            split


splitlines        startswith        strip             swapcase          title


translate         upper             zfill
```

我们可以看到总共有 **`78`** 个方法，魔术方法 **`33`** 个，普通方法 **`45`** 个

***魔术方法 magic method*** 是特殊方法的昵称，在Python中的特殊方法，一般都是使用诸如`__xxx__`（前后两个下划线，中间是方法名）的命名方式，例如：`__init__`、`__class__`。

<br/>

`Python` 也是面向对象编程语言，对于求一个集合的长度使用 `len(list)` 而不是 `list.len()`，背后就是特殊方法的作用，调用了`list.__len__()`方法，和面向对象完全符合，而且还起到简化的作用，变得更加通俗易懂,这就是 `Python` 的简洁体现之一。

<br/>

`Python` 中的魔术方法，在[【Python 高级专栏】](https://juejin.cn/column/6960599942540820493)中有详细介绍，请查看 [Python中的魔法属性](https://juejin.cn/post/6959490821934710797)

<br/>

### 4.2 使用 `help()` 来查看方法、函数的文档

```python
def iter_out(iter_obj, row_num, left_just=18)-> (iter, int):
    """
    指定格式迭代输出
    :param iter_obj: 待输出的可迭代对象
    :param row_num: 一行输出多少个
    :param left_just: 左对齐的宽度
    :return:
    """
    for index in range(len(iter_obj)):
        print(iter_obj[index].ljust(left_just), end='')
        if (index+1) % row_num == 0:
            print()
            print('\n')
            
print(">>>使用help()查看文档")
help(iter_out)
help(str.split)

输出结果:
>>>使用help()查看文档
Help on function iter_out in module __main__:

iter_out(iter_obj, row_num, left_just=18) -> (<built-in function iter>, <class 'int'>)
    指定格式迭代输出
    :param iter_obj: 待输出的可迭代对象
    :param row_num: 一行输出多少个
    :param left_just: 左对齐的宽度
    :return:

Help on method_descriptor:

split(...)
    S.split(sep=None, maxsplit=-1) -> list of strings
    
    Return a list of the words in S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are
    removed from the result.
```

<br/>

> 注意：使用 `help()` 时不要把函数、方法的 **括号 ()** 写进去，因为 `()` 是函数调用

<br/>

### 4.3 字符串常用方法

| 方法名                            | 功能                   |
| --------------------------------- | ---------------------- |
| **`upper(), lower()`**            | 把字符串转成大、小写   |
| **`split()`**                     | 字符串分割             |
| **`startswith()、endswith()`**    | 字符串前、尾部比较     |
| **`replace()`**                   | 字符串替换             |
| **`strip()、lstrip()、rstrip()`** | 去除空格               |
| **`find()`**                      | 在字符串中查找子字符串 |

<br/>

#### 字符串大小写转换upper()、lower()

```python
print(">>>字符串大小写转换upper()、lower()")

lowercase_letters = "a boy can do everything for girl"
capital_letters = "HE IS JUST KIDDING"

print(lowercase_letters.upper())
print(capital_letters.lower())

>>>字符串大小写转换upper()、lower()
A BOY CAN DO EVERYTHING FOR GIRL
he is just kidding
```

<br/>

#### 字符串分割split()

| 方法参数       | 含义                           |
| -------------- | ------------------------------ |
| **`sep`**      | 字符串的 **分割符(separator)** |
| **`maxsplit`** | `maxsplit` 最大分割数，默认-1  |

- **`maxsplit` 最大分割数，默认-1遇到分割符就切割**
- **`maxsplit` 为负数遇到分隔符就切割，0不切割**

<br/>

**`split()` 方法返回值是 `list` 列表**

```python
print(">>>字符串切割spilt()")
content = '123#abc#admin#root'

print(content.split(sep='#', maxsplit=0))
print(content.split(sep='#', maxsplit=1))
print(content.split(sep='#', maxsplit=2))
print(content.split(sep='#', maxsplit=3))
print(content.split(sep='#', maxsplit=4))

print(content.split())  # 不分割，返回list列表

print(content.split('#'))   # 我们习惯这样使用

>>>字符串分割spilt()
['123#abc#admin#root']
['123', 'abc#admin#root']
['123', 'abc', 'admin#root']
['123', 'abc', 'admin', 'root']
['123', 'abc', 'admin', 'root']
['123#abc#admin#root']
['123', 'abc', 'admin', 'root']
```

<br/>

#### 字符串前尾部比较 `startswith()`、`endswith()`

**作用：判断字符串是否以指定字符或子字符串开头**

```python
In [14]: url = 'http://127.0.0.1/index.html'

In [15]: url.startswith('http')
Out[15]: True

In [16]: # 匹配开头

In [17]: url.startswith('http')
Out[17]: True

In [18]: url.startswith('https')
Out[18]: False

In [19]: # 匹配结尾

In [20]: url.endswith('html')
Out[20]: True

In [21]: url.endswith('index')
Out[21]: False
    
```

<br/>

## 五、索引、切片操作字符串

### 5.1 使用索引和切片取单个字符和截取字符串
**切片语法:** `object[start_index:end_index:step]`

| 属性              | 含义     |
| ----------------- | -------- |
| **`start_index`** | 起始索引 |
| **`end_index`**   | 结束索引 |
| **`step`**        | 步长     |

> `step` 正负数均可，而正负号决定了 **“切取方向”**，**正** 表示 **“从左往右”** 取值，**负** 表示 **“从右往左”** 取值。当`step` 省略时，默认为 `1`，即从左往右以增量 `1` 取值.

<br/>

```python
def out_demo_title(title):
    """
    打印案例标题
    :param title
    :return:
    """
    title = " " * 40 + title + " " * 40
    print("-" * 100)
    print(title)
    print("-" * 100)
    
out_demo_title("索引、切片操作字符串Demo")
verify_codes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

print(">>>索引取第一个、最后一个字符")
print(verify_codes[0] + '\t' + verify_codes[len(verify_codes)-1] + '\n')

print(">>>切片取最后一个字符")
print(verify_codes[-1:] + "\n")

print(">>>切片取前26个小写字母")
print(verify_codes[:26] + '\n')    # --> [:26] == [0:26]

print(">>>切片取26个大写字母")
print(verify_codes[26:52] + '\n')

print(">>>切片取后10个数字")

print(verify_codes[-10:] + '\n')  # [-10:]==[len(verify_codes)-10:len(verify_codes)] 

print(">>>切片取前面所有字母")
print(verify_codes[:-10] + '\n')
```

<br/>

### 5.2 for循环遍历字符串

```python
def iter_out(iter_obj, row_num, left_just=18)-> (iter, int):
    """
    指定格式迭代输出
    :param iter_obj: 待输出的可迭代对象
    :param row_num: 一行输出多少个
    :param left_just: 左对齐的宽度
    """
    for index in range(len(iter_obj)):
        print(iter_obj[index].ljust(left_just), end='')
        if (index+1) % row_num == 0:
            print('\n')
            
verify_codes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# for循环遍历字符串
for char in verify_codes:
	print(char)

print('>>>for循环遍历字符串')
iter_out(verify_codes, row_num=10, left_just=11)
```
<br/>

**输出结果：**

```
>>>for循环遍历字符串
a        b        c        d        e        f        g        h        i        j        
k        l        m        n        o        p        q        r        s        t        
u        v        w        x        y        z        A        B        C        D        
E        F        G        H        I        J        K        L        M        N        
O        P        Q        R        S        T        U        V        W        X        
Y        Z        0        1        2        3        4        5        6        7        
8        9
```

有了这个 `iter_out()`自定义的函数是不是打印好看多了

<br/>

## 尾语

**✍ 用  Code 谱写世界，让生活更有趣。❤️**

**✍ 万水千山总是情，点赞再走行不行。❤️**

**✍ 码字不易，还望各位大侠多多支持。❤️**

<br/>

![015.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98268b1254784b0fbd155a7ac103fdba~tplv-k3u1fbpfcp-watermark.image)
