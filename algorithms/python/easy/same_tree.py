#! /usr/bin/env python
# -*- coding:utf-8 -*-

# https://leetcode.com/problems/same-tree/
"""
two binary tree are considered equal if
there are structurally identical and the nodes
have the same value

"""

#Definition for a binary tree node
#class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self. right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: boolean
        """
        while(q != None and p != None):
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and \
                    self.isSameTree(p.right, q.right)
            else:
                return False
        return q == None and  p == None
