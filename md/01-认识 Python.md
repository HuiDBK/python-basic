# 认识 Python

> 人生苦短，我用 Python —— Life is short, you need Python

![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDQvMTMvYzNFMVVIV3JHZVZkak9OLmpwZw?x-oss-process=image/format,png)

<br/>

## 一、 Python 的起源

> Python 的创始人为吉多·范罗苏姆（Guido van Rossum）

![Guido.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51da9dcaa3274bdea5a9b45fb2155465~tplv-k3u1fbpfcp-watermark.image)

<br/>

1. `1989` 年的圣诞节期间，**吉多·范罗苏姆** 为了在阿姆斯特丹打发时间，决心开发一个新的 **解释程序**，作为 `ABC` 语言的一种继承（**牛人就是不一样，动不动就要造语言解释程序**）
2. `ABC` 是由吉多参加设计的一种教学语言，就吉多本人看来，ABC 这种语言非常优美和强大，是**专门为非专业程序员设计的**。但是 ABC 语言并没有成功，究其原因，吉多认为是 **非开放** 造成的。吉多决心在 Python 中避免这一错误，并获取了非常好的效果
3. 之所以选中 **Python（蟒蛇）** 作为程序的名字，是因为他是 `BBC` 电视剧——蒙提·派森的飞行马戏团（Monty Python's Flying Circus）的爱好者
4. `1991` 年，第一个 **Python 解释器** 诞生，它是用 **C 语言实现的，并能够调用 C 语言的库文件**

<br/>

### 解释器

**计算机不能直接理解任何除机器语言(0, 1)以外的语言**，所以必须要把程序员所写的程序语言翻译成机器语言，计算机才能执行程序。**将其他语言翻译成机器语言的工具，被称为编译器**

编译器翻译的方式有两种：一个是 **编译**，另外一个是 **解释**。两种方式之间的区别在于**翻译时间点的不同**。当编译器**以解释方式运行的时候**，也称之为 **解释器**

![编译型和解释型语言工作对比-w360](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDQvMTMvOWVITnBTbjh3a3ZWR2dtLnBuZw?x-oss-process=image/format,png)

<br/>

* **编译型语言**：程序在执行之前需要一个专门的编译过程，把程序编译成为机器语言的文件，运行时不需要重新翻译，直接使用编译的结果就行了。程序执行效率高，依赖编译器，跨平台性差些。如 C、C++
* **解释型语言**：解释型语言编写的程序不进行预先编译，以文本方式存储程序代码，会将代码一句一句直接运行。在发布程序时，看起来省了道编译工序，但是在运行程序的时候，必须先解释再运行

<br/>

**编译型语言和解释型语言对比**

* **速度** —— 编译型语言比解释型语言执行速度快
* **跨平台性** —— 解释型语言比编译型语言跨平台性好

<br/>

**Python 的解释器** 如今有多个语言的实现，包括：

- `CPython` —— 官方版本的 C 语言实现
- `JPython` —— 可以运行在 Java 平台
- `IronPython` —— 可以运行在 .NET 和 Mono 平台
- `PyPy` —— Python 实现的，支持 JIT 即时编译

<br/>

### Python 的设计目标

`1999` 年，**吉多·范罗苏姆** 向 `DARPA` 提交了一条名为 **“Computer Programming for Everybody”** 的资金申请，并在后来说明了他对 `Python` 的设计目标：

* 一门**简单直观的语言**并与潮流语言一样强大
* **开源**，以便任何人都可以为它做贡献
* 代码**像纯英语那样容易理解**
* 适用于**短期**开发的日常任务

这些想法中的基本都已经成为现实，Python 已经成为一门流行的编程语言

<br/>

### Python 的设计哲学

> Python的设计哲学 —— 优雅、简单、哲学。

<br/>

在 Python 解释器内运行 `import this` 可以获得如下完整的Python设计哲学 —— **Python之禅**

```python
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

<br/>

翻译如下

>Python之禅 by Tim Peters
>
>优美胜于丑陋（Python 以编写优美的代码为目标）
>明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
>简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）
>复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
>扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
>间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
>可读性很重要（优美的代码是可读的）
>即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）
>
>不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）
>
>当存在多种可能，不要尝试去猜测
>而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
>虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）
>
>做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
>
>如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）
>
>命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）

<br/>

Python 开发者的哲学是：**用一种方法，最好是只有一种方法来做一件事**

如果面临多种选择，Python 开发者一般会拒绝花俏的语法，而选择**明确没有或者很少有歧义的语法**

<br/>

## 二、给你选择 Python的理由

> 代码量少，第三方库多，人工智能首选语言之一......，同样的问题，用不同的语言解决，代码量差距还是很多的，一般情况下 `Python` 是 `Java` 的 **1/5**，再看看各语言之父的发际量，就知道**人生苦短，我用 Python。**

![各语言之父](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a84813212084cbc9bcaefc44d5e79d4~tplv-k3u1fbpfcp-watermark.image)

<br/>

## 三、Python 特性

* Python 是**完全面向对象的语言**
    * **函数、模块、数字、字符串、类都是对象，在 Python 中一切皆对象**
    * 完全支持继承、重载、多重继承
    * 支持重载运算符，也支持泛型设计
* Python **拥有一个强大的标准库**，Python 语言的核心只包含 **数字**、**字符串**、**列表**、**字典**、**文件** 等常见类型和函数，而由 Python 标准库提供了 **系统管理**、**网络通信**、**文本处理**、**数据库接口**、**图形系统**、**json处理** 等额外的功能
* Python 社区提供了**大量的第三方模块**，使用方式与标准库类似。它们的功能覆盖 **科学计算**、**人工智能**、**机器学习**、**Web 开发**、**数据库接口**、**图形系统** 多个领域

<br/>

**面向对象的思维方式**

* **面向对象** 是一种 **思维方式**，也是一门 **程序设计技术**
* 要解决一个问题前，首先考虑 **由谁** 来做，怎么做事情是 **谁** 的职责，最后把事情做好就行！
    * **对象** 就是 **谁**
* 要解决复杂的问题，就可以找**多个不同的对象**，**各司其职**，共同实现，最终完成需求

<br/>

## 四、Python 的优缺点

### 优点

* 语法简单、上手快易学
* 免费、开源
* **面向对象**
* 拥有丰富的库
* 可扩展性高

<br/>

### 缺点

* 运行速度相对编译型语言更慢
* 国内市场较小
* 中文资料匮乏

<br/>

## 尾语

**✍ 用 Code 谱写世界，让生活更有趣。 ❤️**

**✍ 万水千山总是情，点赞再走行不行。❤️**

**✍ 码字不易，还望各位大侠多多支持。❤️**

<br/>

![001.jpg](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e5ee1181b52470b9a2a78c1b038e3f8~tplv-k3u1fbpfcp-watermark.image)
