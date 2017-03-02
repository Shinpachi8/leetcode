#! /usr/bin/env python3
# coding=utf-8

"""
94% 用python刷这题... 还得考虑到int的最大值，
在强类型中， int是32位， 在［-2147483648， 2147483647］之间
不管是输入还是输出，都不应该超过这个值。
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_value_re = 7463847412
        min_value_re = -8463847412
        max_value = 2147483647
        min_value = -2147483648
        if x >= -9 and x <= 9:
            return x
        if x > max_value_re or x <= min_value_re:
            return 0
        if x > 1000000000 and x % 10 > 2:
            return 0
        if x < -1000000000 and abs(x) % 10 > 2:
            return 0
            
        nagative = True
        if x < 0:
            nagative = False
            x = abs(x)

        result = 0
        while (x):
            result = result * 10 + x % 10
            x = x / 10
        if nagative:
            return 0 if result > max_value else result
        else:
            return 0 if -result < min_value else -result

if __name__ == '__main__':
    x =  -8463847412
    print Solution().reverse(x)
        
        
