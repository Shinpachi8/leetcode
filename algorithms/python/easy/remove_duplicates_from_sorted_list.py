#! /usr/bin/env python
# -*- coding:utf-8 -*-

#https://leetcode.com/problems/remove-duplicates-from-sorted-list/

"""
链表里， 可以用 temp = head， 来复制一下head的内存索引,此时对temp来进行操作，
比如遍历链表进入插入删除时
此时head仍然指向的是链表的头部，用head仍然可以再对链表进行遍历

"""

#definition for singly-linked list
#class ListNode(object):
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
    """
    :type head:ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    else:
        temp = head
        while temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
