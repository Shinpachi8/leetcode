#! /env/bin/python2
# coding=utf-8

"""
beats 96%
"""
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return max(nums)

        max_int = None
        middle_int = None
        third_int = None

        for i in nums:
            print i, [max_int, middle_int, third_int]
            if not max_int:
                max_int = i
            else:
                if i > max_int:
                    if middle_int:
                        if i > middle_int:
                            third_int = middle_int
                            middle_int = max_int
                            max_int = i
                        if i < middle_int:
                            if third_int:
                                if i > third_int:
                                    third_int = i
                            else:
                                third_int = i

                    else:
                        middle_int = max_int
                        max_int = i
                else:
                    if middle_int:
                        if i != max_int:
                            if i > middle_int:
                                third_int = middle_int
                                middle_int = i
                            else:
                                if third_int:
                                    if i != middle_int:
                                        if i > third_int:
                                            third_int = i
                                else:
                                    if i != middle_int:
                                        third_int = i

                        # else:
                        #     if third_int:
                        #         if i != max_int:
                        #             if i > third_int:
                        #                 third_int = i
                        #     else:
                        #         if i != middle_int:
                        #             third_int = i
                    else:
                        if i != max_int:
                            middle_int = i

        # for i in nums:
        #     if not middle_int:
        #         middle_int = i
        #     else:
        #         if i > middle_int:
        #             if max_int:
        #                 if i >= mix_int:
        #                     if third_int:
        #                         third_int = middle_int
        #                         middle_int = max_int
        #                         mix_int = i
        #                     else:
        #                         # 如果没有第三大的数
        #                         third_int = middle_int
        #                         middle_int = max_int
        #                         max_int = i
        #                 else:
        #                     third_int = middle_int
        #                     middle_int = i
        #             else:
        #                 max_int = i
        print third_int, middle_int, max_int
        if third_int is not None:
            return third_int
        else:
            return max_int


if __name__ == '__main__':
    #nums = [1,2,3,2]
    #nums = [5,2,2]
    #nums = [1,2,2,5,3,5]
    #nums = [5,2,4,1,3,6,0]
    nums = [3,3,4,3,4,3,0,3,3]
    print Solution().thirdMax(nums)

