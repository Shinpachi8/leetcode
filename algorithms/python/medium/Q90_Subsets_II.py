#!/usr/bin/env python
# coding=utf-8

"""

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        length = len(nums)
        for i in xrange(length):
            for j in range(i+1, length+1):
                # print i, j
                if nums[i:j] in result:
                    pass
                else:
                    result.append(nums[i:j])
        return result

if __name__ == '__main__':
    nums = [1,2,3]
    print Solution().subsetsWithDup(nums)

