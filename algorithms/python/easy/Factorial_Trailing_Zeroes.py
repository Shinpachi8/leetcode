#! /env/bin/python2
# coding=utf-8

import time
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # [分析]
        # 分解因子, 当且仅当 因子中出现 一对 (2,5)时, 最后结果会增加一个 trailing zero.
        # 1.  2的个数永远多于5个个数.
        # 2.  计算5的个数时, 最简单的方法是 SUM(N/5^1,  N/5^2, N/5^3...)
        if n == 0:
            return 0

        result = 0
        while( n / 5 != 0):
            n = n / 5
            result += n
        return result


        """
        # 以下为自己写的。虽然也可以通过，但是超时！！
        start = time.time()

        if n == 0:
            return 0


        mutil_value = 1
        result = 0
        for i in range(1, n+1):
            while i % 10 == 0:
                result += 1
                i = i / 10
            if i == 1:
                continue
            mutil_value = mutil_value * i
            if mutil_value%10 == 0:
                result += 1
                mutil_value = mutil_value / 10
        # print time.time() - start
        # return result
        str_value = str(mutil_value)
        for i in range(len(str_value), 0, -1):
            if str(i - 1) != "0":
                print time.time() - start
                return  result
            else:
                result += 1


        while mutil_value % 10 == 0:
            result += 1
            mutil_value = mutil_value / 10
        print time.time() - start
        return result
        # return result
        # print mutil_value

        result = 0

        while(mutil_value):
            # result += mutil_value / 10
            if mutil_value % 10 == 0:
                result += 1

                mutil_value = mutil_value / 10
            else:
                return result

        """

if __name__ == '__main__':
    n = 2599
    n2 = 2594
    print Solution().trailingZeroes(n2)







    # ADMIN@123
    # admin@123
