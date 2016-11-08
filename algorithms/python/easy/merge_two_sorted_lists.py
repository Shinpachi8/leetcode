#! /usr/bin/env python
# -*- coding:utf-8 -*-
#https://leetcode.com/problems/merge-two-sorted-lists/

"""
合并两个有序的链表, 合并后还是有序的。
遍历两个链表，找到较小的并进去，一直到两个链表都遍历为止
中间用 temp=ans， 复制了一下新生成链表的头部内存

"""

"""
class ListNode(objects):
    def __init__(self, x):
        self.val = x
        self.next = None
"""

class Solution(object):
    def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None and l2 is None:
        return None
    if l1 and l2 is None:
        return l1
    if l2 and l1 is None:
        return l2

    ans = ListNode(0)
    temp = ans
    while( l1 or l2 ):
        if l1 and l2:
            if l1.val < l2.val:
                tmep.next = l1
                l1 = l1.next
                temp = temp.next
                continue
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next 
                continue
        if l1 and l2 is None:
            temp.next = l1
            break
        if l2 and l1 is None:
            temp.next = l2
            break
    return ans.next


