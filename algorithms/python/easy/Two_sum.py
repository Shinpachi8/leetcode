#! /env/bin/python2
# coding=utf-8


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        real_list = [i for i in nums if i <= target]
        length = len(real_list)
        print real_list
        for i in range(length-1):
            for j in range(i+1, length):
                print i,j,'------>',real_list[i],real_list[j]

                if real_list[i] + real_list[j] == target:
                    #print i,j,'------>',real_list[i],real_list[j]
                    return [i,j]
#-----------------------------------------------------
"""
生成一个字典，将差值为键，对应的下标为值，因为只有一个适配的结果，所以只要匹配上就可以。
class Solution(object):
    def twoSum(self, nums, target):
        \""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        \""
        #real_list = [i for i in nums if i <= target]
        dict_a = {}
        length = len(nums)
        for i in range(length):
            if nums[i] in dict_a:
                return [i, dict_a[nums[i]]]
            else:
                dict_a[target-nums[i]] = i








"""
if __name__ == '__main__':
    nums = [0,4,3,0]
    print Solution().twoSum(nums,0)