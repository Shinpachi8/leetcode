#! /usr/bin/env  python
# -*- coding:utf-8 -*- 


# https://leetcode.com/problems/house-robber/

"""
本来是想的动态规划，但是超时了，于是想用while 循环来做
但是结果一直不对，
因为想错了，将 nums[i]+nums[i+2] > nums[i+1]来循环，这其实是不
对的，应该将max_value 加 nums[i] 与 max_value_pre 比较，
然后再更新值 

"""

class Solution(object):
    """docstring for Solution"""
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenth = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]

        max_value = [0]*length
        max_value[0] = nums[0]
        max_value[1] = nums[0] if nums[0] > num[1] \
            else nums[1]

        i = 2
        while( i < length ):
            max_value[i] = (nums[i] + max_value[i-2]) if \
                (nums[i] + max_value[i-2]) > max_value[i-1] \
                else max_value[i-1]

        return max_value[lengh-1]

//v2
"""
class Solution(object):
    def rob(self, nums):
        \"""
        :type nums: List[int]
        :rtype: int
        \"""
        length = len(nums)
        
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums)
            
        else:
            max_value = 0
            max_value_pre = nums[0]
            max_value_pre2 = nums[0] if nums[0] > nums[1] else nums[1]
            i = 2
            while( i < length):
                max_value = max((nums[i] + max_value_pre), max_value_pre2)
                max_value_pre = max_value_pre2
                max_value_pre2 = max_value
                i += 1

            return max_value
"""