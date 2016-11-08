#! /usr/bin/env python
# -*- coding:utf-8 -*-

#https://leetcode.com/problems/power-of-two/

class Solution(object):
    def isPowerOfTwo(self, n):
    """
    :type n: int
    :rtype: boolean
    """
    if n < 0:
        return False
    s = bin(n)
    if s.count("1") == 1:
        return True
    else:
        return False
