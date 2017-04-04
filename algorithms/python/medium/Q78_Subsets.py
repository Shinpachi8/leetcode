#!/usr/bin/env python
#coding=utf-8

"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


nums=[1,2]
result = [[]]
第一轮， result = [[], [1]]
第二轮， result = [[], [1], [2], [1,2]]
可以看出对于每添加一个数，都是用result的前一轮的值添加此数，然后与前一轮的结果做并。
这样可以用迭代的方法


解法2
也可以通过位操作的方式来。如果有n个数，那么其子集有2^n -1 个。 对应为 0-2^n-1, 可以对应到比特位上。即
n位的元素，如果下标对应1， 说明此数在子集中.

"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]

        for i in nums:
            result += [tmp + [i] for tmp in result]
        return result

    def subset2(self, nums):
        result = []
        length = len(nums)
        total = pow(2, length) - 1
        while(total >= 0):
            n = 0
            tmp_total = total
            tmp = []
            while (n < length):
                if tmp_total >> n & 0x1 == 1:
                    tmp.append(nums[n])
                n += 1
            result.append(tmp)
            total -= 1
        return result



if __name__ == '__main__':
    nums = [1,2,3]
    print Solution().subset2(nums)
