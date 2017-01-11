#!/usr/bin/env python
# coding=utf-8

"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_int, count1 = 0, 0
        l2_int, count2 = 0, 0
        l11 = l1
        while l1:
            l1_int = 10 * l1_int + l1.val
            count1 += 1
            l1 = l1.next

        l22 = l2
        while l2:
            l2_int = 10 * l2_int + l2.val
            count2 += 1
            l2 = l2.next

        # count1 = count1 if count1 > count2 else count2
        maxa = count1 if count1 > count2 else count2


        tmp_result = l1_int + l2_int
        str_result = str(tmp_result)

        if len(str_result) - maxa == 1:
            head = ListNode(0)
            if maxa == count1:
                head.next = l11
            else:
                head.next = l22
        else:
            if maxa == count1:
                head = l11
            else:
                head = l22

        result = head
        for i in str_result:
            head.val = int(i)
            head = head.next
        return result



        # result_int = 0
        # print tmp_result

        # while tmp_result:
        #     result_int = 10 * result_int + tmp_result % 10

        #     tmp_result = tmp_result / 10

        # result = ListNode(0)
        # head = result
        # print result_int
        # if result_int == 0:
        #     return result
        # else:
        #     while result_int:
        #         v = result_int % 10
        #         tmp = ListNode(v)
        #         head.next = tmp
        #         head = head.next
        #         result_int = result_int / 10

        #     return result.next

if __name__ == '__main__':
    a = ListNode(7)
    b = ListNode(2)
    c = ListNode(4)
    d = ListNode(3)

    e = ListNode(5)
    f = ListNode(6)
    g = ListNode(4)

    a.next = b
    b.next = c
    c.next = d

    e.next = f
    f.next = g

    a1 = ListNode(5)
    b1 = ListNode(5)

    # # print a.next.val
    # while a:
    #     print a.val
    #     a = a.next


    result = Solution().addTwoNumbers(a1, b1)
    while result:
        print result.val
        result = result.next
