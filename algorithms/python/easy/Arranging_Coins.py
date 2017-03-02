#! /usr/bin/env python3
# coding=utf-8

# 10%
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        x = 1
        while True:
            if (x * (x + 1)) / 2 < n:
                x += 1
                continue
            elif (x * (x + 1)) / 2 == n:
                return x
            else:
                return x - 1
        # if n == 0:
        #     return 0
        # x = 1
        # while True:
        #     n -= (2 * x - 1)
        #     if n > x + 1:
        #         x += 1
        #         continue
        #     elif n == x + 1:
        #         return x + 1
        #     else:
        #         return x

if __name__ == '__main__':
    n = 2146664525
    print Solution().arrangeCoins(n)

