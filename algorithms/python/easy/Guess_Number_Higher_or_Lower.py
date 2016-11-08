#! /env/bin/python2
# coding=utf-8


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher,otherwise return 0
# def guess(num):
from time import sleep
def guess(num):
    if num > Random_value:
        return -1
    elif num < Random_value:
        return 1
    else:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(n) == 0:
            return n

        half = n / 2
        least = 0

        result = guess(half)
        while (result != 0):
            sleep(1)
            if result == -1:
                n = half
            if result == 1:
                least = half
            print "result is {}, half is {}, n is {}, least is {}".format(result, half, n, least)
            half = (n + least) / 2
            result = guess(half)
        
        return half

if __name__ == '__main__':
    n = 1000
    Random_value = 50
    print Solution().guessNumber(n)