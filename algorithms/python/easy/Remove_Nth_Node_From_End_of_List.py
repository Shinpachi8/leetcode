# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None and n == 1:
            return []
        length = self.count(head)
        if length == n:
            return head.next

        temp = head
        while temp.next:
            if self.count(temp.next) == n:
                temp.next = temp.next.next
                break
            else:
                temp = temp.next
        return head

    def count(self, root):
        length = 1
        while root.next:
            length += 1
            root = root.next
        return length
