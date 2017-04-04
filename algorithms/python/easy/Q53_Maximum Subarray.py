#!/usr/bin/env python
# coding=utf-8

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

Solution: https://discuss.leetcode.com/topic/5000/accepted-o-n-solution-in-java/2

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not A:
        #     return 0

        # curSum = maxSum = A[0]
        # for num in A[1:]:
        #     curSum = max(num, curSum + num)
        #     maxSum = max(maxSum, curSum)

        # return maxSum

        # 首先判断到目前为止，要不要加上后边的那个值，
        # 再判断这时候与最大值哪个较大

        MaxSoFar =  MaxEndPoint = nums[0]
        for i in nums[1:]:
            MaxSoFar = max(MaxSoFar + i, i)
            MaxEndPoint = max(MaxSoFar, MaxEndPoint)
        return MaxEndPoint

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print Solution().maxSubArray(nums)


