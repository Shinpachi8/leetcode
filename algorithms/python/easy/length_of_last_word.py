#! /usr/bin/env python
# -*- coding:utf-8 -*- 

#https://leetcode.com/problems/length-of-last-word/
"""
目前这种解法有点问题，是非常慢的
想了一种算法是从后往前数，遇到' ' 就pass
然后遇到字母就 加1 如果最后没有+ ，就返回0 否则返回length


"""
class Solution(object):
    def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """

    s = s.rstrip()
    length = 0
    totole = len(s)

    for i in range(0, totole):
        if s[i] == ' ' and i == totole - 1:
            return length
        length += 1

        if s[i] == ' ' and i < tototle - 1:
            length = 0
    return length


