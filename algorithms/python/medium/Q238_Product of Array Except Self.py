#!/usr/bin/env python
# coding=utf-8

"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

Subscribe to see which companies asked this question

"""

# 构造 两个列表，分别从前往后，从后往前乘，这样就把中间的错过了。
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        res = [1] * length
        i = 1
        while i < length:
            res[i] = res[i-1] * nums[i-1]
            i += 1

        right = 1
        while length > 0:
            res[length - 1] = res[length - 1] * right
            right *= nums[length - 1]
            length -= 1

        return res

if __name__ == '__main__':
    nums = [1,2,3,4]
    print Solution().productExceptSelf(nums)





