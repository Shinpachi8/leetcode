#!/usr/bin/env python
#coding=utf-8

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

这里一个动态规划题，可以在这里看分析
https://discuss.leetcode.com/topic/15265/0ms-5-lines-dp-solution-in-c-with-explanations
很清楚。
也就是说，如果我们在m[1][2], 那么它的步数只等于到达它上边或者左边的频数的和。
即: m[i][j] = m[i-1][j] + m[i][j-1]
这就是动态规划的最主要的公式

还有两种解法，现在还没理解 。
//TODO： 理解一下更优化的解法
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = [([0] * m) for i in xrange(n)]
        print result
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        print len(result[0])
        for i in xrange(m):
             result[0][i] = 1
        print result
        for j in xrange(n):
            result[j][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                result[j][i] = result[j-1][i] + result[j][i-1]
                print result

        return result[n-1][m-1]

if __name__ == '__main__':
    print Solution().uniquePaths(3,4)
