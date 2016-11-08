#! /usr/bin/env python
# -*- coding:utf-8 -*-

# https://leetcode.com/problems/happy-number/

"""
如果是haay number的话，会停止在1上， 而
如果不是， 刚会进入一循环中，所以做一个set，
set中出现了重复的数， 就表示不是happy number

"""
class Solution(Object):
    def isHappy(self, n):
        if n == 1:
            return True
        if n == 0:
            return False

        collection = set()
        while (n != 1):
            temp = 0
            while( n != 0 ):
                temp += pow(n%10, 2)
                n /= 10
            if temp in collection:
                return False
            else:
                collection.add(temp)
                n = temp
        return True
