# Python 字典 — dict

## 字典的定义

- `dict`（字典） 是 **除列表以外** `Python` 之中 **最灵活** 的数据类型
- 字典同样可以用来 **存储多个数据**
  - 通常用于存储 **描述一个 `物体` 的相关信息** 
- 和列表的区别
  - **列表** 是 **有序** 的对象集合
  - **字典** 是 **无序** 的对象集合
- 字典用 `{}` 定义 或者 `dict()`
- 字典使用 **键值对** 存储数据，键值对之间使用 `,` 分隔
  - **键** `key` 是索引
  - **值** `value` 是数据
  - **键** 和 **值** 之间使用 `:` 分隔
  - **键必须是唯一的**
  - **值** 可以取任何数据类型，但 **键** 只能使用 **字符串**、**数字**或 **元组**

<br/>

```python
xiaoming = {
    "name": "小明",
    "age": 18,
    "gender": True,
    "height": 1.75
}
```

<br/>

![字典示意图](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbc894d3d4b748df976ee070fc4a81ee~tplv-k3u1fbpfcp-watermark.image)

 

<br/>

## 字典常用操作

- 在 `IPython` 中定义一个 **字典**，例如：`goods_dict= {}`
- 输入 `goods_dict.` 按下 `TAB` 键，`IPython` 会提示 **字典** 能够使用的方法如下：

![字典常用方法](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b52b8936d4e45b7adb25f008a8c00f4~tplv-k3u1fbpfcp-watermark.image)

<br/>

各方法的用处，在上图中已说明了，这里选几个**常用方法/操作**测验一下。

### 字典定义

```python
In [81]: # 空字典定义

In [82]: goods_dict = {}

In [83]: goods_dict2 = dict()

In [84]: type(goods_dict)
Out[84]: dict

In [85]: type(goods_dict2)
Out[85]: dict
```

<br/>

```python
In [86]: # 带有数据的字典定义
                                       ^
In [88]: goods_dict ={'name': '掘金T恤', 'price': 59}

In [89]: goods_dict2 = dict(name='掘金T恤', price=59)

In [90]: type(goods_dict), type(goods_dict2)
Out[90]: (dict, dict)

In [91]: goods_dict
Out[91]: {'name': '掘金T恤', 'price': 59}

In [92]: goods_dict2
Out[92]: {'name': '掘金T恤', 'price': 59}
```

<br/>

### 字典添加数据

```python
In [94]: goods_dict
Out[94]: {'name': '掘金T恤', 'price': 59}

In [95]: # 添加数据
In [96]: goods_dict['size'] = 'L'

In [97]: goods_dict
Out[97]: {'name': '掘金T恤', 'price': 59, 'size': 'L'}
```

<br/>

### 字典删除数据

```python
In [102]: goods_dict
Out[102]: {'name': '掘金T恤', 'price': 59, 'size': 'L'}

In [103]: # 删除指定键数据

In [104]: del goods_dict['size']

In [105]: goods_dict
Out[105]: {'name': '掘金T恤', 'price': 59}

In [106]: goods_dict.pop('price')
Out[106]: 59

In [107]: goods_dict
Out[107]: {'name': '掘金T恤'}

In [108]: goods_dict.popitem()
Out[108]: ('name', '掘金T恤')

In [109]: goods_dict
Out[109]: {}
```

<br/>

`del goods_dict[key]、goods_dict.pop(key)`  都是指定**键key**，删除字典内的键值对。

- `del` 没有返回值，`pop()` 返回当前删除键的**值**

`goods_dict.popitem()` 则是随机删除字典内一个键值对，并返回删除的**键值对**。

<br/>

```python

In [111]: goods_dict
Out[111]: {'name': '掘金T恤', 'price': 59}

In [112]: # 清空字典数据

In [113]: goods_dict.clear()

In [114]: goods_dict
Out[114]: {}
```

<br/>

### 字典更新数据

```python
In [116]: goods_dict
Out[116]: {'name': '掘金T恤', 'price': 59}

In [117]: # 更新字典数据

In [118]: goods_dict['name'] = '掘金徽章'

In [121]: goods_dict
Out[121]: {'name': '掘金徽章', 'price': 59}

In [122]: goods_dict.setdefault('price', 18)
Out[122]: 59

In [123]: goods_dict
Out[123]: {'name': '掘金徽章', 'price': 59}

In [124]: goods_dict.setdefault('size', 'M')
Out[124]: 'M'

In [125]: goods_dict
Out[125]: {'name': '掘金徽章', 'price': 59, 'size': 'M'}
```

<br/>

可以发现字典中的 `setdefault()` 方法，当字典中已存在相对应的键时不会更新其键的值，只能用于增加键值对，而 **字典[key]** ，如果 **key** 存在则更新，不存在则新增。

<br/>

```python
In [127]: goods_dict
Out[127]: {'name': '掘金徽章', 'price': 59, 'size': 'M'}

In [128]: # 整体更新

In [130]: new_info = {'price': 18, 'size': '5cm'}

In [131]: goods_dict.update(new_info)

In [132]: goods_dict
Out[132]: {'name': '掘金徽章', 'price': 18, 'size': '5cm'}

In [133]: new_info = {'name': '掘金小册xx', 'author': 'hui', 'price': 19.9}

In [134]: goods_dict.update(new_info)

In [135]: goods_dict
Out[135]: {'name': '掘金小册xx', 'price': 19.9, 'size': '5cm', 'author': 'hui'}
```

<br/>

字典中的 `update(新字典)` 方法则是将新字典中合并到原字典中。有相同的键则更新，没有的键则新增。

<br/>

### 字典获取指定键的值

```python
In [137]: goods_dict
Out[137]: {'name': '掘金小册xx', 'price': 19.9, 'size': '5cm', 'author': 'hui'}

In [138]: # 获取指定键的值

In [139]: goods_dict['name']
Out[139]: '掘金小册xx'

In [140]: goods_dict['author']
Out[140]: 'hui'

In [141]: goods_dict.get('price')
Out[141]: 19.9

In [142]: goods_dict['id']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-142-b8a93fe9ad6b> in <module>
----> 1 goods_dict['id']

KeyError: 'id'

In [145]: ret = goods_dict.get('id')

In [147]: print(ret)
None

In [148]: count = goods_dict.get('count', 0)

In [149]: count
Out[149]: 0
```

 <br/>

使用 `字典[key]` 当字典中的 `key` 不存在时会报错，`字典.get(key)` ，当键不存在时则默认返回 `None`，可以更改默认返回值，如 `goods_dict.get('count', 0)` ，获取商品数量当键不存在时默认为0.

<br/>

### 其他

```python
In [154]: goods_dict
Out[154]: {'name': '掘金小册xx', 'price': 19.9, 'author': 'hui'}

In [155]: # 字典中键值对的数量

In [156]: len(goods_dict)
Out[156]: 3

In [157]: # 获取字典中的所有的 key

In [158]: goods_dict.keys()
Out[158]: dict_keys(['name', 'price', 'author'])

In [161]: # 获取字典中的所有的 value

In [162]: goods_dict.values()
Out[162]: dict_values(['掘金小册xx', 19.9, 'hui'])

In [163]: # 字典中所有的键值对(元组列表)

In [164]: goods_dict.items()
Out[164]: dict_items([('name', '掘金小册xx'), ('price', 19.9), ('author', 'hui')])
```

<br/>

## 字典循环遍历

- **遍历** 就是 **依次** 从 **字典** 中获取所有键值对

```python

In [167]: for key in goods_dict:
     ...:     print('key', key)
     ...:     print('value', goods_dict[key])
     ...:     print()
     ...:
     ...:
key name
value 掘金小册xx

key price
value 19.9

key author
value hui
```

 <br/>

`for ... in ...` 默认取字典中的 `keys()` 所有的键 ，然后再通过键获取值。

然而我们可以通过字典中的 `items()` 来一次遍历键和值

```python
In [168]: for key, value in goods_dict.items():
     ...:     print(key, value)
     ...:     print()
     ...:
     ...:
name 掘金小册xx

price 19.9

author hui
```

<br/>

## 应用场景

- 尽管可以使用 `for in` 遍历 **字典**
- 但是在开发中，更多的应用场景是：
  - 使用 **多个键值对**，存储 **描述一个 `物体` 的相关信息** —— 描述更复杂的数据信息
  - 将 **多个字典** 放在 **一个列表** 中，再进行遍历，在循环体内部针对每一个字典进行 **相同的处理**

```python
info_list = [
    {
        "name": "hui",
     	"qq": "222815",
     	"phone": "10010"
    },
             
    {
        "name": "zack",
        "qq": "54321",
        "phone": "10086"
    },
    
    {
        "name": "wang",
        "qq": "12345",
        "phone": "10000"
    }
             
]

```

<br/>

## 尾语

**✍ 用  Code 谱写世界，让生活更有趣。❤️**

**✍ 万水千山总是情，点赞再走行不行。❤️**

**✍ 码字不易，还望各位大侠多多支持。❤️**

<br/>

![018.jpg](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be80c1f202e84ac4a704b870fcdb4f7c~tplv-k3u1fbpfcp-watermark.image)
