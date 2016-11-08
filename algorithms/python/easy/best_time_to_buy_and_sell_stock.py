#! /usr/bin/env python
# -*- coding:utf-8 -*-

#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
题意理解: 给定一个列表， 找到其中正差最大
记录最小值， 如果 i 个值比最小值大，那么记算他与最小值之间的差，和当前的利润
值相比，两者取其中最大的
否则更新最小值

"""

class Solution(object):
    def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0:
        return 0
    if len(set(prices)) == 1:
        return 0
    temp = prices[::]
    if tmep.sort(reverse=True) == temp:
        return 0 

    ans, mins = 0, prices[0]
    for i in prices:
        if i > mins:
            ans = max(ans, i-mins)
        else:
            mins = i
    return ans
