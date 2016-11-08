#! /env/bin/python2
# coding=utf-8

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        length = len(nums)
        count = 0
        for i in range(length):
            if val ^ nums[i] == 0:
                nums[i] = -1
            else:
                count += 1
        
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i] < nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]

        return count

#-------------------------------------------------------
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        length = len(nums)
        count = 0
        for i in range(length):
            if val != nums[i]:
                nums[count] = nums[i]
                count += 1

        return count

if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    print Solution().removeElement(nums,val)