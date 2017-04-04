#!/usr/bin/env python
# coding=utf-8

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


这里用的空间复杂度是O(N^2)并浊 O(n)，O（n）的解法我还不理解


public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        for(int i = triangle.size() - 2; i >= 0; i--)
            for(int j = 0; j <= i; j++)
                triangle.get(i).set(j, triangle.get(i).get(j) + Math.min(triangle.get(i + 1).get(j), triangle.get(i + 1).get(j + 1)));
        return triangle.get(0).get(0);
    }
}
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        result = [[0] * (length + 1) for length in xrange(len(triangle))]
        times = len(result)
        for i in xrange(times):
            if i == 0:
                result[0][0] = triangle[0][0]
            else:
                for j in xrange(len(result[i])):
                    # print triangle[i][j],
                    if (j == 0):
                        result[i][j] = result[i-1][0] + triangle[i][0]
                    elif (j == i):
                        result[i][j] = result[i-1][j-1] + triangle[i][j]
                    else:
                        result[i][j] = min(result[i-1][j], result[i-1][j-1]) + triangle[i][j]
        mins = result[times - 1][0]
        for i in result[times-1]:
            if i < mins:
                mins = i
        return mins
        # while time >= 0 :
        #     tmp = time2
        #     if time == (len(result) -1):
        #         while tmp >= 0:
        #             result[time] += triangle[tmp][-1]
        #             tmp -= 1
        #     if time == 0:
        #         while tmp >= 0:
        #             result[time] += triangle[tmp][0]
        #             tmp -= 1

        #     result[time] = min(result[time - 1]



if __name__ == '__main__':
    triangle = [[-1],[3,2],[-3,1,-1]]
    print Solution().minimumTotal(triangle)
