#! /env/bin/python2
# coding=utf-8



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        # 去除开始的与值相等的元素
        while(head):
            if head.val == val:
                if head.next:
                    head = head.next
                else:
                    return []
            else:
                break
        temp_head = head
        while(temp_head.next):
            # 如果头部下一个节点的值和要目标值相等 , 判断是否
            # 有下一个的下一个， 如果没有，则将下一个节点的下一个置0
            if temp_head.next.val == val:
                if temp_head.next.next:
                    temp_head.next = temp_head.next.next
                else:
                    temp_head.next = None
            else:
                temp_head = temp_head.next

        
        return head