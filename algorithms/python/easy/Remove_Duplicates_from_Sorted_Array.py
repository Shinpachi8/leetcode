#! /bin/env/python2
# coding=utf-8


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        count = 0
        i = 0
        mark = 0
        for i in range(length-1):
            if i < mark:
                continue
            while mark <= length - 1:
                if nums[mark] == nums[i]:
                    mark += 1
                else:
                    nums[count] = nums[i]
                    count += 1
                    break
        
        print mark
        nums[count] = nums[-1]
        print nums
        return count+1 


if __name__ == '__main__':
    nums = [1,1,3,3,2]
    print Solution().removeDuplicates(nums)


        