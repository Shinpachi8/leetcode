#! /usr/bin/env python
# -*- coding:utf-8 -*-


#https://leetcode.com/problems/swap-nodes-in-pairs/

"""
这题是将相邻的两个链节点，对换，  1->2->3->4 改成 2->1-4->3
想的是用栈，每压入两节点， 就弹出两个节点，这样顺序正好对了。
但是在实现的时候一直是在死循环中。
解决办法:  将弹出的节点的下一节点置为空。
"""


#Definition for singly-linked list
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        stack = []
        ans = ListNode(0)
        temp = ans
        count = 0

        while(head):
            stack.append(head)
            head = head.next
            count += 1
            if count == 2:
                while(count > 0):
                    temp2 = stack.pop()
                    temp2.next = None
                    temp.next = temp2
                    temp = temp.next
                    count -= 1

        if len(stack) == 1:
            temp.next = stack.pop()
            temp = temp.next

        return ans.next


"""
这种是家桦的算法，没有用到栈，只是用到了两个变量，
在python的运行在比我的快。
学习一下
"""

class Solution(object):
    def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    newHead = ListNode(0)
    curNode = ListNode(0)

    while(head is not None and head.next is not None):
        temp = head.next
        head.next = head.next.next
        temp.next = head
        curNode.next = temp
        curNode = head
        head = head.next

    curNode.next = head
    return newHead.next
