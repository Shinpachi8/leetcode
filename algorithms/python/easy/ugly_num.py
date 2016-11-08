#! /bin/usr/env python
# -*- coding:utf-8 -*-

#https://leetcode.com/problems/ugly-number/

"""
包含的素数因子只有 2，3，5，的数叫做丑数
而如果含的合数因子，还可以在最后拆成素数相乘， 即，丑数是只包含
2，3，5因子的数。
如果拆开之后有 除 2，3，5 之外的素数，就是说并不是丑数

"""

class Solution(Object):
    def isUgly(self, num):
        if num <= 0:
            return False
        if num == 1:
            return True
       # add this , can beat 90% if not add this, can beat 30%
        if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
            return False
        else:
           while(num % 2 == 0):
                num /= 2  # 将因子2全部排除
            while(num % 3 == 0):
                num /= 3 # 将因子3 全部排除
            while(num % 5 == 0):
                num /= 5 
            if num == 1:
                return True
            else:
                return False

