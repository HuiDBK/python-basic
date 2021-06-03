# PyCharm使用介绍及常用配置

## Python 的 IDE —— `PyCharm`

### 1） 集成开发环境（IDE）

***集成开发环境（IDE，Integrated Development Environment）*** —— 集成了开发软件需要的大部分工具。一般包括以下工具：

- 图形用户界面
- 代码编辑器（支持 **代码补全**／**自动缩进**）
- 编译器／解释器
- 调试器（**断点**／**单步执行**）
- ……

 <br/>

### 2）PyCharm 介绍

- `PyCharm` 是 Python 的一款非常优秀的集成开发环境
- `PyCharm` 除了具有一般 IDE 所必备功能外，还可以在 `Windows`、`Linux`、`macOS` 下使用
- `PyCharm` 适合开发大型项目
  - 一个项目通常会包含 **很多源文件**
  - 每个 **源文件** 各司其职，共同完成复杂的业务功能

 <br/>

## PyCharm上手使用

### 创建Python项目

我们以后都以 `PyCharm` 进行编程演示，接下来介绍一些 `PyCharm` 使用常识。

![PyCharm创建Python项目](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f64e5272bbb24ce69c55ac5b8835c199~tplv-k3u1fbpfcp-watermark.image)

<br/>

创建 `Python` 项目的一些配置

![创建Python项目向导](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46362fb1d68f4d5784f2d866b5e1fa90~tplv-k3u1fbpfcp-watermark.image)

<br/>

创建 `Python` 项目就介绍到这，接下来就用 `PyCharm` 打开我们之前创建的 `Python-Basic` 目录。

![PyCharm窗口介绍](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ae8035680fc4d578a0b2d9035f56664~tplv-k3u1fbpfcp-watermark.image)

<br/>

> 运行 `Python` 程序要先在 **代码编辑区** 右击在弹出的菜单项中点击 `Run`，或者使用快捷键 `Shift + F10`，之后就可以点击 **运行按钮 ▶**。

<br/>

### 新建Python文件

在当前项目目录 `Python-Basic` 右击选择 `New -> Python file` 即可新建 `Python` 文件

![创建Python文件](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b75f9f0a06a436a9ca6baaafad2ed71~tplv-k3u1fbpfcp-watermark.image)

<br/>

## PyCharm常用设置

> 因为 `PyCharm` 是全英文版，可能对英语不太好的小伙伴使用起来会没有那么上手，不要怕一步一步来，等你用久了，慢慢摸索就熟悉了。但要记住一些常用的设置，其他设置等你想到了再去百度搜索即可。

<br/>

### 设置窗口主题样式

在 `PyCharm` 的菜单栏上点击 `File -> settings`，进入 **PyCharm配置界面** 然后找到 `Appearance` 选项

<br/>

![PyCharm主题设置](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e82ab1b09b64211a8ad423d30e8f045~tplv-k3u1fbpfcp-watermark.image)

<br/>

### 设置文件字体大小

在 `PyCharm` 的菜单栏上点击 `File -> settings`，进入 **PyCharm配置界面** 然后找到 `Editor` 选项下 `Font` 

![PyCharm设置文件字体配置](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66b01f7c1032444aa5e09a98827cb560~tplv-k3u1fbpfcp-watermark.image)

<br/>

### 设置项目Python解释器

还是一样先进入PyCharm配置界面。

- 可以在菜单栏 `File -> settings...` 进入然后选择 `Project:项目名` 下 `Python Interpreter` 选项。
- 也可以在 `PyCharm` 右下角点击 `Python` 字样选择 `Interpreter Setttings`

![右下角进入Python解释器设置](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef6dc8e05bdb47f296e551b78017fdb2~tplv-k3u1fbpfcp-watermark.image)

<br/>

![项目Python解释器设置](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbeb99ac35ea4a73bae3d78432bcb9bd~tplv-k3u1fbpfcp-watermark.image)

<br/>

> **解释器所下载的库/包** 右边有一个 `+` 号按钮，用于 **添加新的 Python库/包 到当前解释器内**。

<br/>

### 设置Python文件、代码模板风格

> 打开配置界面 `File -> settings...`，找到 `Editor` 配置选项，进行如下设置

![设置Python文件、代码模板](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c7dbe52a115439996cc55bad76d342e~tplv-k3u1fbpfcp-watermark.image)

<br/>

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 模块描述 }
# @Date: ${YEAR}/${MONTH}/${DAY} ${TIME}


def main():
    pass
    

if __name__ == '__main__':
    main()
    
```

<br/>

这是我个人的风格爱好，大家可以根据自己爱好来设置。下次新建 `Python` 文件都会是如下风格

![使用模板后的Python文件](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52114bd532fa4dfdb92664b54c967353~tplv-k3u1fbpfcp-watermark.image)

<br/>

## 尾语

**✍ 用  Code 谱写世界，让生活更有趣。❤️**

**✍ 万水千山总是情，点赞再走行不行。❤️**

**✍ 码字不易，还望各位大侠多多支持。❤️**

<br/>

![005.jpg](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9efb6e33af1541ba86f1189f8002cae6~tplv-k3u1fbpfcp-watermark.image)