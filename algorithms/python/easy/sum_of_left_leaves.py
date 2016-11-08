#! /env/bin/python2
# coding=utf-8


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
首先这个节点是一个叶子节点，同时还是父节点的左子节点
所以要用 note.left is not None and note.left is None and note.right is None
"""
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.total = 0
        
        self.calculate(root)
        return self.total
        
    def calculate(self, root):
        if root is None:
            return
        if root.left and root.left.left == None and root.left.right == None:
            self.total += root.left.val
        
        self.calculate(root.left)
        self.calculate(root.right)
