#! /env/bin/python2
# coding=utf-8

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_a = {}
        for i in s:
            if i in dict_a:
                dict_a[i] += 1
            else:
                dict_a[i] = 1
        
        length = len(s)
        for i in range(length):
            if dict_a[s[i]] == 1:
                return i
        
        return -1