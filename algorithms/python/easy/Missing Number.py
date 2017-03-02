#!/usr/bin/env python
# coding=utf-8

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        # method1
        sum_of_n = 0
        for i in range(len(nums) + 1):
            sum_of_n += i

        return sum_of_n - sum(nums)

        """

        # method2， 用XOR， 这样会把除剩下那个选出来, 先将res置最大，len(nums)， 然后分别与下标和值做异或
        res = len(nums)
        for index, value in enumerate(nums):
            res ^= index
            res ^= value
        return res

