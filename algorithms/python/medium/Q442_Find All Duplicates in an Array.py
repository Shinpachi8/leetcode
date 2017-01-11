#!/usr/bin/env python
# coding=utf-8

"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        i = 0
        result = []
        if nums == "":
            return result
        while i <= 2:
            for index, value in enumerate(nums):
                print "nums[index]:{}, nums[value - 1]:{}".format(value, nums[value-1])
                if index + 1 == value:
                    continue
                elif nums[value - 1] ==value:
                    continue
                else:
                    nums[index], nums[value - 1] = nums[value - 1], nums[index]
            i += 1
        for index, value in enumerate(nums):
            if index + 1 != value and nums[value - 1] == value:
                result.append(value)

        print result
"""
解法2:
对于每一位，将对应下标的值标为负，然后
取它的绝对值来查看下标，如果是负，那么就是出现了两次。


"""

if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    # nums = [7, 2, 3, 4, 1, 2, 3, 8]
    Solution().findDuplicates(nums)
