#!/usr/bin/env python
# coding: utf-8

"""
url: https://leetcode.com/problems/max-consecutive-ones/?tab=Description
author: shinpachi8
date: 17/03/02
version: 1.0
Question: 485
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, result = 0, 0, 0
        start = False
        for index, value in enumerate(nums):
            if value == 1:
                if not start:
                    left = index
                    start = True
            else:
                # print result, (index - left)
                if start:
                    result = result if result > (index - left) else (index - left)
                    start = False
                    left = index
        if start:
            result = result if result > (len(nums) - left) else (len(nums) - left)
        return result

if __name__ == '__main__':
    nums = [1,1,0,1,1,1,1,1,1,0,0,1]
    print Solution().findMaxConsecutiveOnes(nums)
