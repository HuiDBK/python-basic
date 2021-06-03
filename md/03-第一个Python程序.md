# 我的第一个Python程序

## 引言

> `Python` 环境安装好了，可以进行Python程序编写了，但在哪里编写Python程序呢？是在 `cmd` 窗口中输入`Python` 打开的Python交互器编写吗？还是在记事本中？刚入门都可以，但还是建议先用记事本来编写。到后面有专门的Python开发工具 `PyCharm`。

<br/>

## Python 源程序概念

- `Python` 源程序就是**一个特殊格式的文本文件**，可以**使用任意文本编辑软件**做 `Python` 的开发

- `Python` 程序的 **文件扩展名** 通常都是 `.py`

<br/>

## 创建 `Python-Basic` 工作目录

> 在桌面创建 `Python-Basic` 工作目录，其中 `Python-Basic` 的意思就是Python基础。这个目录专门用来存放练习Python基础所编写的文件。

<br/>

### 创建 `01-hello.py` 文件

在 `Python-Basic` 目录中创建 `01-hello.py` 文件并用记事本打开，写入如下代码

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-


print('hello python')
print('hello world')
```

<br/>

其中 `#!/usr/bin/python3` 是声明在 `Linux` 中使用 `Python3` 解释器运行该文件。

而 `# -*- coding:utf-8 -*-` 则是声明该文件以 `utf-8` 形式编码。在 `Python3` 中这一行可有可无，因为`Python3` 中默认以 `unicode` 编码方式存储，而 `Python2` 则是以 `ASCII` 编码方式存储，Python2中如果文件中出现了中文会造出乱码现象，因此要在开头声明文件的编码方式。

我们这是在 `Windows` 平台上使用 `Python3` 解释器，可以不写这两行，**但我个人建议写上这两行，培养良好代码习惯**。代码习惯和风格不是一朝一夕能练成的，因此从基础做起。可能你现在不理解，没事的，很多事情都是**后知后觉**，没必要一开始就弄的一清二楚，等嫣然回首，能让你恍然大悟足以。所以开始上手觉得麻烦你可以直接复制粘贴，照猫画虎。

<br/>

> `Python3, Python2` 指的是Python解释器的版本。
>
> Python3是指版本为 `Python 3.x`的解释器，Python2则是版本为 `Python 2.x` 的解释器。
>
> **Python 3.x 是现在和未来主流的版本**

<br/>

扯了这么多，该回归主题了，编写完 `Python` 代码该如何运行呢？

你可以尝试一下双击运行，但这样简单的双击是看不到运行效果的

<br/>

### cmd 窗口运行Python程序

之前说过 `Python` 代码要 **Python解释器** 才能解释运行。由于我们在安装 **Python环境** 的时就把Python解释器的路径添加到了 **系统环境变量-Path** 中，因此我们可以在 **cmd 窗口输入Python调用Python解释器**。

<br/>

在当前 `Python-Basic` 目录中打开 `cmd` 窗口

![当前目录打开cmd.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/896f576c22f74c61aa1e46a018071656~tplv-k3u1fbpfcp-watermark.image)

<br/>

输入如下指令即可调用 **Python解释器** 运行 `Python` 程序。

```cmd
python 01-hello.py
```

<br/>

![cmd运行python程序.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94a63040afb04990967f33dc53ee91ee~tplv-k3u1fbpfcp-watermark.image)

<br/>

`python` 后面接的是要 **运行文件的路径**，由于我是在当前目录中打开的 `cmd` 窗口，所以只要输入文件名字即可。这里也可以不用输入完整的文件名称，例如：输入 `01` 然后按下 `tab` 键会自动补全文件名称。

如果不是在当前目录打开的 `cmd` ，请记得把文件的路径写完整。 

<br/>

> `print()` 函数的作用，可以把 **`" "`** 内部的内容，输出到屏幕上。

<br/>

### 双击 `python` 文件运行

首先并不是双击运行不了，只要有 `Python` 环境，并配置了系统环境变量都是可以运行，只是运行效果太快了，一闪而过，根本看不到运行结果。因此只要在文件中添加 **延时、堵塞、死循环** 等操作都可看见运行效果，这里就教你们使用  `input()` 函数来堵塞程序。

<br/>

新建 `02-input.py` 文件，输入如下代码

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-


print('input() 函数练习')

ret = input('请输入测试内容: ')
print(ret)

input('输入任意字符退出程序')
```

<br/>

双击程序就可看见如下运行效果

![input运行结果.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c48eaf1075d747418c7c7fb96da295da~tplv-k3u1fbpfcp-watermark.image)

<br/>

> `input()` 函数括号里面填写你要在屏幕显示的提示信息，`input()` 函数会让Python程序堵塞，等待你输入数据，并把你输入的数据当做返回值，我这里是用 `ret` 变量接收。

<br/>

如果双击还是不能运行，可能是因为你有多个 **Python解释器** 或者默认打开 `.py` 的后缀文件不是Python解释器，这个只要把打开方式指定为默认以 **Python解释器（Python.exe）** 运行即可。

<br/>

## 错误（BUG）演练

### 关于错误

- 编写的程序**不能正常执行**，或者**执行的结果不是我们期望的**
- 俗称 `BUG`，是程序员在开发时非常常见的，初学者常见错误的原因可能包括如下几点：
  1. 手误
  2. 对已经学习过的知识理解还存在不足
  3. 对语言还有需要学习和提升的内容
- 在学习语言时，不仅要**学会语言的语法**，而且还要**学会如何认识错误和解决错误的方法**

<br/>

> 每一个程序员都是在不断地修改错误中成长的，失败乃成功之母，不要害怕错误。

<br/>

### 常见错误

:writing_hand:  **手误**，例如使用 `pirnt("hello python")` 

```python
NameError: name 'pirnt' is not defined

错误解释 -> 名称错误：'pirnt' 名字没有定义
```

<br/>

:writing_hand:  将多条 `print` 写在一行 `print('hello') print('python')`

```python
SyntaxError: invalid syntax

错误解释 -> 语法错误：语法无效
```

> 每行代码负责完成一个动作

<br/>

:writing_hand: **缩进错误**

```python
IndentationError: unexpected indent

错误解释 -> 缩进错误：不期望出现的缩进
```

> - Python 是一个格式非常严格的程序设计语言
> - 目前而言，大家记住每行代码前面都不要增加空格

<br/>

### 常见错误单词

```python
* error 错误
* name 名字
* defined 已经定义
* syntax 语法
* invalid 无效
* Indentation 缩进
* Index 索引
* unexpected 意外的，不期望的
* character 字符
* line 行
* encoding 编码
* declared 声明
* details 细节，详细信息
* ASCII 一种字符编码
```

<br/>

## 尾语

**✍ 用  Code 谱写世界，让生活更有趣。❤️**

**✍ 万水千山总是情，点赞再走行不行。❤️**

**✍ 码字不易，还望各位大侠多多支持。❤️**

<br/>

![003.jpg](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58983b210919444486b76fb50a99638a~tplv-k3u1fbpfcp-watermark.image)

