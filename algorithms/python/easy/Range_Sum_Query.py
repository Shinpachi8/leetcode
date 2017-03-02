#! /usr/bin/env python3
# coding=utf-8

"""
参考别人的解法

v1 建立一个直方图，相当于直接操纵一个数组， beat 5%
v2 优化了一下， beat 98%

"""
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """

        length = len(nums)
        self.nums = [0] * length
        self.nums[0] = nums[0]
        for i in range(1, length):
            self.nums[i] = self.nums[i-1] + nums[i]


        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.nums[j]
        else:
            return self.nums[j] - self.nums[i-1]


   





    #    v1:  5%   
    #     length = len(nums)
    #     self.nums = [0] * length
    #     for i in range(0, length):
    #         self.nums[i] = sum(nums[0: i + 1])


        

    # def sumRange(self, i, j):
    #     """
    #     sum of elements nums[i..j], inclusive.
    #     :type i: int
    #     :type j: int
    #     :rtype: int
    #     """
    #     if i == 0:
    #         return self.nums[j]
    #     else:
    #         return self.nums[j] - self.nums[i-1]
        


if __name__ == '__main__':
    nums = [0,1,2,3,4,5,6]
    a = NumArray(nums)
    print a.sumRange(0,1)
    print a.sumRange(1,4)
    print a.sumRange(0,3)
    print a.sumRange(2,5)
    print a.sumRange(1,5)

