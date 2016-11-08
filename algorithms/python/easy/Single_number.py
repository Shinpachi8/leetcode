#! /env/bin/python2
# coding=utf-8

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 0:
            return
        
        temp = {}
        for i in nums:
            if i in temp:
                temp.pop(i)
            else:
                temp[i] = 1
        return temp.popitem()[0]

"""
如果两个数相同，那么异或与为0，否则为1，只要一直异或下去，剩下的那个就是单独的
class Solution(object):
    def singleNumber(self, nums):
        \"""
        :type nums: List[int]
        :rtype: int
        \"""
        x = 0
        for i in nums:
            x = i ^ x
        
        return x


"""

if __name__ == '__main__':
    a = [2,2,1,1,4,3,3]
    print Solution().singleNumber(a)
