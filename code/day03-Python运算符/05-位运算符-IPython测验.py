#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 位运算符 IPython测验 }
# @Date: 2021/06/07 20:18

# bin()函数简单使用
"""
In [6]: bin(10)
Out[6]: '0b1010'

In [7]: bin(8)
Out[7]: '0b1000'
"""


# 按位与、按位或，位运算符测验
"""
In [0]: # 按位与 &
In [1]: bin(10)
Out[1]: '0b1010'

In [2]: bin(8)
Out[2]: '0b1000'

In [3]: a = 10

In [4]: b = 8

In [5]: a & b
Out[5]: 8

In [6]: bin(a & b)
Out[6]: '0b1000'

In [7]: # 按位或 |

In [8]: a | b
Out[8]: 10

In [9]: bin(a | b)
Out[9]: '0b1010'
"""


# 按位异或、按位取反，位运算符测验
"""
In [10]: # 按位异或 ^

In [11]: a = 10

In [12]: b = 8

In [13]: bin(a)
Out[13]: '0b1010'

In [14]: bin(b)
Out[14]: '0b1000'

In [15]: a ^ b
Out[15]: 2

In [16]: bin(a ^ b)
Out[16]: '0b10'

In [17]: # 按位取反 ~

In [18]: a = 13

In [19]: bin(a)    # 0000 1101
Out[19]: '0b1101'

In [20]: bin(~a)   # 1111 1110 带符号位的2进制补码呈现
Out[20]: '-0b1110'

In [21]: ~a
Out[21]: -14
"""


# 左移动、右移动，位运算符测验
"""
In [27]: # 左移 <<
In [27]: a = 10

In [28]: bin(a)
Out[28]: '0b1010'    # 0000 1010

In [29]: bin(a << 2)
Out[29]: '0b101000'  # 0010 1000

In [30]: a << 2
Out[30]: 40

In [31]: # 右移 >>

In [32]: b = 7

In [33]: bin(7)		
Out[33]: '0b111'    # 0000 0111

In [34]: bin(b >> 2)
Out[34]: '0b1'      # 0000 0001 

In [35]: b >> 2
Out[35]: 1
"""
