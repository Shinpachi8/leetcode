#!/usr/bin/env python
# coding: utf-8


"""
URL:https://leetcode.com/problems/find-bottom-left-tree-value/?tab=Description
第一种解法，是用这种层次搜索
第二种 可以用queue
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = [root.val, 0]
        if root.left is None and root.right is None:
            return root.val

        elif root.left is None:
            self.result = [root.right.val, 1]
            self.gotleft(root.right, 1)
        elif root.right is None:
            self.result = [root.left.val, 1]
            self.gotleft(root.left, 1)
        else:
            self.result = [root.left.val, 0]
            self.gotleft(root.left, 1)
            self.gotleft(root.right, 1)
        return self.result[0]


    def gotleft(self, root, level):
        if root.left is None and root.right is None:
            if level > self.result[1]:
                self.result = [root.val, level]

            return 0
        elif root.left is None:
            if level > self.result[1]:
                self.result = [root.right.val, level]
            self.gotleft(root.right, level + 1)
        elif root.right is None:
            if level > self.result[1]:
                self.result = [root.left.val, level]
            self.gotleft(root.left, level + 1)
        else:
            # self.result = [root.left.val, level]
            self.gotleft(root.left, level + 1)
            self.gotleft(root.right, level + 1)
