#! /usr/bin/env python3
# coding=utf-8


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if k == 0:
            pass
        elif k > length:
            pass
        else:
            temp = []
            for i in range(length-1, -1, -1):
                if length - 1 - i < k:
                    temp.append(nums[i])
                else:
                    nums[i + k] = nums[i]
            for i in range(k):
                nums[i] = temp[k-1-i]
        print nums

if __name__ == '__main__':
    nums = [1,2]
    k = 3
    print Solution().rotate(nums, k)
