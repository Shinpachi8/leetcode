#!/usr/bin/env python
# coding: utf-8

"""
url:https://leetcode.com/problems/minimum-size-subarray-sum/?tab=Description
author:  shinpachi8
date: 17/03/01
version: 1.0

"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        left, total, result = 0, 0, len(nums) + 1
        for right, val in enumerate(nums):
            total += val
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0





if __name__ == '__main__':
    nums = [1,2,3,4,5]
    s = 15
    print Solution().minSubArrayLen(s, nums)
