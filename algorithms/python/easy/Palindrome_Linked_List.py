#! /env/bin/python2
# coding=utf-8

# Definition for singly-linked list.


"""
对于链表的操作，一个是链表的逆。
另外一个是链表的中间节点
可以用上下两个指针来操作。一个每次都走2个节点，另一个走1个
这样等走的快的指针到链尾时，那么走的慢的正好到中间
31%

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
this beats 83%
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        down = head
        reverse_head = ListNode(0)
        reverse_head.val = head.val
        temp = ListNode(0)
        while(head.next):
            if head.next.next:
                head = head.next.next
                temp.val = down.next.val
                down = down.next
                temp.next = reverse_head
                reverse_head = temp
                temp = ListNode(0)
            else:
                down = down.next
                break

        while (down.next and reverse_head.next):
            if down.val != reverse_head.val:
                return False
            down = down.next
            reverse_head = reverse_head.next
        if down.val != reverse_head.val:
            return False
        else:
            return True



"""
class Solution(object):
    def isPalindrome(self, head):
        """
        #:type head: ListNode
        #:rtype: bool
        """
        if head is None:
            return True
        if head.next == None:
            return True

        up = head

        down = head
        reverse_head = ListNode(0)
        
        reverse_head.val = head.val
        

        while(up.next):
            print "in here"
            if up.next.next:
                up = up.next.next
                temp = ListNode(0)
                temp.val = down.next.val
                down = down.next
                temp.next = reverse_head
                print reverse_head.val, "vallllll"
                reverse_head = temp
                
                print reverse_head.val
                print reverse_head.next.val
                
            else:
                down = down.next
                break
        print "OUT here"
        tt = down
        while(tt.next):
            print tt.val
            tt = tt.next
        print tt.val
        while (down.next and reverse_head.next):
            #print "in here again"
            print "down.val:{}\t reverse_head.val:{}".format(down.val, reverse_head.val)
                
            if down.val != reverse_head.val:
                return False
            down = down.next
            reverse_head = reverse_head.next

        if down.val != reverse_head.val:
            return False
        else:
            return True

"""

if __name__ == '__main__':
    #list_value = [-31900,22571,-31634,19735,13748,16612,-28299,-16628,9614,-14444,-14444,9614,-16628,-31900,16612,13748,19735,-31634,22571,-28299]

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(2)
    e = ListNode(1)
    # d = ListNode(19735)
    # e = ListNode(13748)
    # f = ListNode(16612)
    # g = ListNode(-28299)
    # h = ListNode(-16628)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    if Solution().isPalindrome(a):
        print "Yes"
    else:
        print "NO"    