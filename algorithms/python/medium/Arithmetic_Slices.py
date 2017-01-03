#!/usr/bin/env python
# coding=utf-8


"""
一开始没想出来，其实是我想复杂了。这就是一个求等差数列，只要判断前后几个就可以了。
并不是要求跳着来.. 如 [1,2,3,5,7] 这样有连续的[1,2,3] 而我当时想的是
[1,5,6,8,3,9,5] 找到 ［1, 3, 5］...

"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        index = 1
        lens = 0
        result = 0
        while index < length - 1:
            if A[index] - A[index-1] == A[index + 1] - A[index]:
                lens += 1
                print lens
            else:
                if lens > 0:
                    result += lens * (lens + 1) / 2
                    lens = 0
            index += 1
        if lens > 0:
            result += lens * (lens + 1) / 2
        return result






if __name__ == '__main__':
    A = [1,2,3,4,5,7,9]
    print Solution().numberOfArithmeticSlices(A)
