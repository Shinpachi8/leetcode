#! /usr/bin/env python
# coding=utf-8

"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp_dic = {}
        result = []
        # tmp_list = [0] * (nums /2 + 1)
        for i in nums:
            if i in tmp_dic:
                tmp_dic[i] += 1
            else:
                tmp_dic[i] = 1
        for i in tmp_dic:
            if tmp_dic[i] == 1:
                result.append(i)

        return result
# method 2  解决了我一直想解决的,就是在异或之后，如何将两个值挑出来。
"""
1. 首先把所有的值做异或， for(num in nums): a = a^num
2. 取最后一个bit。  (a & (a-1)) ^ a
3. 将列表中每一个值与这一个bit做异或，两个值应该是不相同的。分别为n1,n2

"""


if __name__ == '__main__':
    nums = [1,2,1,3,2,4,5,5]
    print Solution().singleNumber(nums)

