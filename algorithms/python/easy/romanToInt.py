#! /env/bin/python2
# coding=utf-8


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_a = {"M":1000,"C":100,"D":500,"L":50,"X":10,"I":1,"V":5}
        length = len(s)

        result = 0
        for i in range(length):
            if i == length - 1:
                result += dict_a[s[i]]
            else:
                if dict_a[s[i]] < dict_a[s[i+1]]:
                    result += -dict_a[s[i]]
                else:
                    result += dict_a[s[i]]

        return result


if __name__ == '__main__':
    s = "DCXXI"
    print Solution().romanToInt(s)
        