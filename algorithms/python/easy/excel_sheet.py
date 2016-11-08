#! /usr/bin/env python
# -*- coding:utf-8 -*-

# https://leetcode.com/problems/excel-sheet-column-number/

class Solution(object):
    def titleToNumber(self, s):
    """
    :type s: str
    :rtype: int
    """
    # a better solution is define temp=ord('A') and replace tt = tt+1
    length = len(s)
    if length == 1:
        return ord(s) - ord('A') + 1
    else:
        for i in range(0, length):
            tt = ord(s[i]) - ord('A')
            sum += pow(26, length-1)*(tt+1)
            length -= 1
        return sum
