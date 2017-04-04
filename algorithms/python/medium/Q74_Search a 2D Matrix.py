#!/usr/bin/env python
#coding=utf-8


"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)
        if (m == 0):
            return False
        else:
            n = len(matrix[0])
            if n == 0:
                return False

        i_row = 0
        for i in xrange(m):
            if matrix[i][n-1] == target or matrix[i][0] == target:
                return True
            if matrix[i][n-1] >= target:
                i_row = i
                break

        else:
            high, low, medium = n - 1, 0, (n - 1) / 2
            while low < high:
                if matrix[i_row][medium] < target:
                    low = medium + 1
                    medium = (low + high) / 2
                elif matrix[i_row][medium] == target:
                    return True
                else:
                    high = medium - 1
                    medium = (low + high) / 2
            return False

if __name__ == '__main__':
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    # target = 2
    matrix = [[1]]
    target = 1
    if Solution().searchMatrix(matrix, target):
        print "Find"
    else:
        print "Not Find"





