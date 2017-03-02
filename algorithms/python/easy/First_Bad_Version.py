#! /usr/bin/env python3
# coding=utf-8


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

"""
beat 97%
"""
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isBadVersion(x):
            if x >= 1702766719:
                return True
            else:
                return False

        temp = n
        high = n
        low = 0
        while True:
            if isBadVersion(temp):
                
                high = temp
                temp = (temp + low) / 2
                #print("temp:{}\t temp/2:{}\t high:{}\t".format(temp, temp/2, high))
                
            else:
                if isBadVersion(temp + 1):
                    return temp + 1 
                else:
                    #print("temp:{}\t temp/2:{}\t high:{}\t".format(temp, temp/2, high))
                    low = temp
                    temp = (temp + high) / 2



if __name__ == '__main__':
    n = 2126753390
    print Solution().firstBadVersion(n)