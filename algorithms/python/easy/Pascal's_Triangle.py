#! /usr/bin/env python3
# coding=utf-8

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []
        
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1],[1,1]]
        
        result = [[1], [1,1]]
        
        for i in range(2, numRows):
            temp = [1,1]
            for j in range(1, i):
                temp_int = result[i-1][j-1] + result[i-1][j]
                temp.insert(j,temp_int)
            result.append(temp)
        return result
