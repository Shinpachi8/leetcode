#! /usr/bin/env python
# -*- coding:utf-8 -*-

#https://leetcode.com/problems/climbing-stairs/

"""
比如 有n 阶台阶，那么我们在n-1阶时，只有一种方法，即走一步
在  n-2 阶时，同样有一种方法，即走2步， 因为走一步的话就是n-1了，
所以 f(n) = f(n-1) + f(n-2)
即可以有递归，但是发现递归超时

那么我们可以从第一阶开始，只有一种方法，第二阶有2种，第3阶有 1+2=3 阶，
第4阶有 2+3=5种  这是斐波那契数列
可以用while来实现
"""

class Solution(object):
    def climbStaris(self, n):
    """
    :type n: int
    :rtype: int
    """
    x = 1
    ans, ans_left = 1,  0
    while( x < n ):
        ans, ans_left = ans + ans_left, ans
        x += 1
    return ans
