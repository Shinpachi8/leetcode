#! /env/bin/python2
# coding=utf-8


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp_int = 0
        dupli = x
        while dupli:
            temp_int = 10 * temp_int + (dupli % 10)
            print "dupli%10 is {}, dupli/10 is {}, temp_int is {}".format(dupli%10, dupli/10, temp_int)
            dupli = dupli / 10

        print temp_int


if __name__ == '__main__':
    x = 123321
    Solution().isPalindrome(x)
        