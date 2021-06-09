#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 石头剪刀布小案例 }
# @Date: 2021/06/09 22:16
import random

player = input('请出拳 石头（1）／剪刀（2）／布（3）: ')

player = int(player)

computer = random.randint(1, 3)

if (player == 1 and computer == 2) or \
        (player == 2 and computer == 3) or \
        (player == 3 and computer == 1):

    print('玩家赢了，电脑弱爆了！！！')
elif player == computer:
    print('心有灵犀一点通，平局')
else:
    print('电脑赢了, 不行我要和你决战到天亮')

