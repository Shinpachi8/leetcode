#! /usr/bin/evn python
# -*- coding:utf-8 -*-

#https://leetcode.com/submissions/detail/65017903/

class Solution(object):
    def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    
    """
    # solution 1:    the better one
    if nums1 is None or nums2 is None:
        return None
    else:
        length1, length2 = len(nums1), len(nums2)
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        rtype = []
        p1 = p2 = 0
        while (p1 < length1) and (p2 < length2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                rtype += nums1[p1]
                p1 += 1
                p2 += 1
        return rtype

    # solution 2 :  the worse one 
    """
    if nums1 is None or nums2 is None:
        return []
    else:
        temp = set.intersection(set(nums1), set(nums2))
        if temp is None:
            return None
        else:
            rtype = []
            for i in temp:
                rtype += [i] * min(nums1.count(i), nums2.count(i))

            return rtype


