#!/usr/bin/env python
# coding=utf-8

"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(numbers)-1
        # i = 1
        # while i < len(numbers):
        #     if numbers[0] + numbers[i] == target:
        #         return [1, i+1]
        #     elif numbers[0] + numbers[i] > target:
        #         end = i
        #         break
        #     i += 1
        # if end is None:
        #     end = len(numbers)-1
        # print start, end
        while start <= end:
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                return [start+1, end+1]

if __name__ == '__main__':
    # numbers = [5,25,75]
    # target = 100
    # print Solution().twoSum(numbers, target)





