#!/usr/bin/env python
# coding: utf-8

"""
Total Accepted: 59220
Total Submissions: 139724
Difficulty: Medium
Contributors: Admin
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.


1. 可以用二分法来搜索。如果n=10,那么我选5，如果比5小的个数>=5,那么 就出现在 [1-5]中。
2. 还有一种方法是可以用双链表的方式来搞。用快慢指针。先用快的，再用慢的，这样他们会在同一个地点相遇。
slow = nums[slow], fast = nums[nums[slow]] 好像是这样吧
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        upper = len(nums) - 1
        lower = 1

        while lower < upper:
            mid = (lower + upper) / 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                lower = mid + 1
            else:
                upper = mid
            # print "lower: {}, upper:{}, mid:{}".format(lower, upper, mid)
        return lower

if __name__ == '__main__':
    nums = [1, 1]
    print Solution().findDuplicate(nums)
