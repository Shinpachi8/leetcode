#!/usr/bin/env python
# coding = utf-8

"""
url:https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/?tab=Description

Total Accepted: 29175
Total Submissions: 54802
Difficulty: Easy
Contributors: yuhaowang001


Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

"""





class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        # method1

        for i in range(4):
            for index, value in enumerate(nums):
                if index == value - 1:
                    continue
                else:
                    if nums[value - 1] == value:
                        continue
                    else:
                        nums[value - 1], nums[index] = nums[index], nums[value - 1]
        print nums
        result = []
        for index, value in enumerate(nums):
            if value != index + 1:
                result.append(index + 1)
        return result

        """
        for index, value in enumerate(nums):
            tmp = abs(value)
            if nums[tmp - 1] > 0:
                nums[tmp - 1] = - nums[tmp - 1]

        result = []
        for index, value in enumerate(nums):
            if value > 0:
                result.append(index + 1)
        return result


if __name__ == '__main__':
    nums = [2,3,4,5,6,7,8,1]
    print Solution().findDisappearedNumbers(nums)
