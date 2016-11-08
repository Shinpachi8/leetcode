#! /usr/bin/env python
# -*- coding:utf-8 -*- 


#https://leetcode.com/submissions/detail/65014045/

class Solution(object):
    """
    :type nums: List[int]
    :rtype: boolean
    """

    length = len(nums)
    if length <= 1:
        return False
    length_set = len(set(nums))
    if length_set < length:
        return True
    else:
        return False
