#! /usr/bin/env python3
# coding=utf-8

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # v2  65%
        if n <= 2:
            return 0
        if n == 3:
            return 1
        if n == 4:
            return 2

        prime = [True] * ((n)/2)
        prime[0] = False
        for i in range(len(prime)/2):
            if prime[i]:
                for j in range(i, len(prime), 2*i+1):
                    prime[j] = False
                prime[i] = True

        count = 0
        for i, j in enumerate(prime):
            if j:
                count += 1
                print 2*i + 1
        return count + 1





        # # v1    8%
        # if n <=2:
        #     return 0
        # prime = [True] * ()
        # prime[0] = False
        # prime[1] = False
        # #print len(prime)
        # for i in range(2, n, 2):
        #     prime[i] = False
        # prime[2] = True

        # for i in range(2, n/2):
        #     if prime[i]:
        #         for j in range(2*i, n, i):
        #             prime[j] = False

        # count = 0
        # for i, j in enumerate(prime):
        #     if j:
        #         count += 1
        #         #print i
        # return count






if __name__ == '__main__':
      n = 6
      print Solution().countPrimes(n)  