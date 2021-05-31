# Python环境的搭建与安装

## 引言

> 当我们编写 `Python` 代码时，我们得到的是一个包含 `Python` 代码的以`.py`为扩展名的文本文件。要运行代码，就需要 **Python解释器** 去执行`.py`文件。

<br/>

通常我们将Python和Java语言归为解释型语言，而对于C/C++则归为编译型语言。



![编译、解释型原理](https://img-blog.csdnimg.cn/20200411150818307.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

![编译型和解释型语言工作对比-w360](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pLmxvbGkubmV0LzIwMjAvMDQvMTMvOWVITnBTbjh3a3ZWR2dtLnBuZw?x-oss-process=image/format,png)

<br/>

> 解释器（英语：Interpreter），是一种电脑程序能够把高级编程语言一行一行直接转译运行。解释器不会一次把整个程序转译出来，只像一位“中间人”，每次运行程序时都要先转成另一种语言再作运行，因此解释型的程序运行速度相对编译型更缓慢

<br/>


## 安装Python解释器

### 最新版本下载

- **[官网下载(https://www.Python.org/)](https://www.Python.org/)**

- **选择最新的Python版本以及操作系统（<font color='#FF0057' size=4em>Window举例</font>）**

![Python下载](https://img-blog.csdnimg.cn/20200411151031270.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

<br/>

### 网盘下载

> 如果Python官网进不去或者网速慢，我已上传`Python-3.8.2`和`Python-3.7.5-amd64`，`64位版本`的Python在百度云盘，望能帮助到。

<br/>

| 资源               | 链接                                                         | 提取码   |
| ------------------ | ------------------------------------------------------------ | -------- |
| Python-3.8.2       | [https://pan.baidu.com/s/1aZnk1ooo3qyIQrqyly6ULQ](https://pan.baidu.com/s/1aZnk1ooo3qyIQrqyly6ULQ) | **ea9k** |
| Python-3.7.5-amd64 | [https://pan.baidu.com/s/10bYfA1_JjzFXtSDuQ3lBug](https://pan.baidu.com/s/10bYfA1_JjzFXtSDuQ3lBug) | **tc3t** |

<br/>

### 其他版本下载

- **[查看Python所有版本 (https://www.Python.org/downloads/)](https://www.Python.org/downloads/)**

- **<font color='#FF0057'>以Python 3.7.5版本举例</font>**

    ![查看Python所有版本](https://img-blog.csdnimg.cn/20200411153418231.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70#pic_center) **找到对应的Python版本**
    
    
    
    ![选择Python版本](https://img-blog.csdnimg.cn/20200411153239667.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70#pic_center)
    
    <br/>
    
    **点击Download跳转到下载界面，然后一直滑到 <font color='#FF0057'>Files段落</font>** 
    
    
    
    ![选择Python安装方式](https://img-blog.csdnimg.cn/20200411153000692.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70#pic_center)
    
    
    
    - `X86`和`X86-64`的区别：系统是`32 位 `的版本还是 `64位`
    
    - **web-based**: 透过网络安装的，就是执行安装后再透过网络下载Python
    
    - **executable**: 可执行文件的，既把要安装的Python全部下载好在本机安装
    
    - **embeddable zip file**: zip 压缩包，就是Python打包成了zip压缩包

<br/>


**根据电脑的位数来选择对应的安装程序，点击链接下载，然后选择保存文件的路径**

   ![选择保存文件的路径](https://img-blog.csdnimg.cn/20200411152843312.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70#pic_center)

  <br/>

**请注意，Python 3.5+不能在Windows XP或更早版本上使用。**

<br/>

### 安装Python

**Python 3.8.2 版本举例**

双击打开下载好的`Python-3.8.2.exe`安装程序

勾选`Add Python 3.8 to PATH`这是因为Windows会根据一个`Path`的环境变量设定的路径去查找`Python.exe`，如果没找到，就会报错。

![安装Python](https://img-blog.csdnimg.cn/20200411152520349.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70#pic_left)

**如果在安装时漏掉了勾选`Add Python 3.8 to PATH`，那就要手动把`Python.exe`所在的路径添加到Path中。**

<br/>

`Install Now` 默认安装在C盘，尽量不要安装到C盘，因为安装在C盘我们不好找，C盘东西多了，电脑性能会变慢。我们选择自定义安装

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200411152646652.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70#pic_left)


直接Next

<br/>

**勾选Install for all users，并自定义安装路径**

![自定义Python安装路径](https://img-blog.csdnimg.cn/20200411152320119.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70#pic_left)
点击Install等待进度条走完

<br/>

![等待Python安装](https://img-blog.csdnimg.cn/20200411152237268.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70#pic_left)

<br/>

**安装完成**

![Python安装完成](https://img-blog.csdnimg.cn/20200411152208231.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70#pic_left)

<br/>

## 检测是否安装成功

`Win + R` 键输入 `cmd` 打开**命令提示符窗口** ，在 `cmd` 窗口中输入 `Python` 查看版本并进入**Python交互式环境**

![打开命令提示符窗口](https://img-blog.csdnimg.cn/20200411152009484.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70#pic_center)

<br/>

![检查Python](https://img-blog.csdnimg.cn/20200411152101516.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70#pic_left)

看到上面画面，说明Python安装成功。

<br/>

### 打印 Hello World

你看到提示符`>>>`就表示我们已经在Python交互式环境中了，可以输入任何Python代码，回车后会立刻得到执行结果。

```python
print("Hello World")
```

<br/>

![打印Hello World](https://img-blog.csdnimg.cn/20200411151430878.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjI5ODU3,size_16,color_FFFFFF,t_70)

输入`exit()或quit()`并回车，就可以退出Python交互式环境。

<br/>

## 尾语

**✍ 用代码谱写世界，让生活更有趣。   &nbsp;❤️**

**✍ 万水千山总是情，点赞再走行不行。❤️**

**✍ 码字不易，还望各位大侠多多支持。❤️**

<br/>

![002.jpg](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5fe9a9f24c44203905f53357a8d5853~tplv-k3u1fbpfcp-watermark.image)
