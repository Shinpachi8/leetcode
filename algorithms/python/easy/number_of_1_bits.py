#! /usr/bin/env python
# -*- coding:utf-8 -*-

#https://leetcode.com/submissions/detail/65088758/

class Solution(object):
    def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int

    """
    s = bin(n)
    ans = s.replace("0","")
    return len(ans) - 1
