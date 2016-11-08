"""
#! /env/bin/python
# coding=utf-8
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
对于这个题，考点的数的遍历，其实觉得这个题可以用DFS来解决，但是如何控制深度呢？
还可以考虑一下。
应该想一下树的遍历，其实也不一定再重写一个函数，在原来的函数里其实也是可以实现的
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        self.result = []
        self.result.append([root.val])
        self.get_result(root,1)
        return self.result
    def get_result(self, root, i):

        # 如果左右节点都存在
        if root.left and root.right:
            # 如果结果长度在深度之上时
            if len(self.result) >= i+1:
                self.result[i].append(root.left.val)
                self.result[i].append(root.right.val)
            else:
            # 如果未到达这个深度
                self.result.append([root.left.val, root.right.val])
            self.get_result(root.left, i+1)
            self.get_result(root.right, i+1)
            return

        if root.left and not root.right:
            if len(self.result) >= i+1:
                self.result[i].append(root.left.val)
            else:
                self.result.append([root.left.val])
            self.get_result(root.left, i+1)
            return

        if root.right and not root.left:
            if len(self.result) >= i+1:
                self.result[i].append(root.right.val)
            else:
                self.result.append([root.right.val])
            self.get_result(root.right, i+1)
            return

