#！ /usr/bin/env python
# -*- coding:utf-8 -*-

"""
given two arrays, write a function to compute their intersection

Example:
Given nums1 = [1,2,2,1], nums2 = [2,2], return [2]

Note:
    Each element in the result must be unique
    the result can be in any order
"""


class Solution(object):
    def intersection(self, nums1, nums2)
    """
    :type nums1: list[int]
    :type nums2: list[int]
    :rtype : list[int]
    """

        if nums1 is None or nums2 is None:
            return None
        else:
            returun list(set.intersection(set(nums1), set(nums2)))
