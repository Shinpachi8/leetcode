#!/usr/bin/env python
# coding: utf-8

"""
url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?tab=Description
author: shinpachi8
date: 17/03/02
version: 1.0

找子序列，如果上升就保存，如果下降就抛出
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        result, keep = 0, 0
        for index, value in enumerate(prices):
            if prices[index + 1] > value:
                continue
            else:
                result += value - prices[keep]
                result -= prices[index + 1]
                keep = index + 1
        return result
