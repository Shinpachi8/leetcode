#! /usr/bin/env python3
# coding=utf-8

"""
beat 81%
"""
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        CHAR = ["A", "B", "C", "D", "E", "F", "G",
            "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
            "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        if n <= 26:
            return CHAR[n - 1]

        count = 0
        temp = ""
        result = ""
        count = n / 26
        n = n - count * 26
        # 如果n==0, 说明 26整除n, 那么进位就应该少一， 因为有一位26已经在最后一位为z了。
        if n == 0:
            temp += "Z"
            count -= 1
        else:
            temp += CHAR[n - 1]

        while (count > 26):
            #  如果
            x = count % 26
            count = count / 26
            if x == 0:
                temp += "Z"
                count -= 1
            else:
                temp += CHAR[x - 1]
        if count > 0:
            temp += CHAR[count - 1]
        # 结果取逆
        for i in range(len(temp), 0, -1):
            result += temp[i - 1]
        return result

if __name__ == '__main__':
    n = 1000000004
    print Solution().convertToTitle(n)

