#! /env/bin/python2
# coding=utf-8


"""
@version 1.0
@author jxy
@beat 4&
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        copy1 = root
        copy2 = root
        return self.judge(copy1,copy2)
        
    def judge(self, root1, root2):
        
        if root1.left:
            if not root2.right:
                return False
            else:
                if root1.left.val != root2.right.val:
                    return False
                else:
                    if not self.judge(root1.left, root2.right):
                        return False
        else:
            if root2.right:
                return False

        if root1.right:
            if not root2.left:
                return False
            else:
                if root1.right.val != root2.left.val:
                    return False
                else:
                    if not self.judge(root1.right, root2.left):
                        return False
        else:
            if root2.left:
                return False
        
        # return True        
        if root1.val == root2.val:
            return True
        else:
            return False

"""
@version 1.1
@beat 28%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        copy1 = root
        copy2 = root
        return self.judge(copy1,copy2)
        
    def judge(self, root1, root2):
        
        if root1.left and root2.right:
            if not self.judge(root1.left, root2.right):
                return False
        elif root1.left and not root2.right:
            return False
        elif not root1.left and root2.right:
            return False
                
        if root1.right and root2.left:
            if not self.judge(root1.right, root2.left):
                return False
        elif root1.right and not root2.left:
            return False
        elif not root1.right and root2.left:
            return False
            
        
        if root1 and root2 and root1.val == root2.val:
            return True
        else:
            return False
"""

"""
@verion 1.2
@beat 61%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        copy1 = root
        copy2 = root
        return self.judge(copy1,copy2)
        
    def judge(self, root1, root2):
        
        
        if root1.left and not root2.right:
            return False
        elif not root1.left and root2.right:
            return False
        elif root1.left and root2.right:
            if not self.judge(root1.left, root2.right):
                return False
                
        
        if root1.right and not root2.left:
            return False
        elif not root1.right and root2.left:
            return False
        elif root1.right and root2.left:
            if not self.judge(root1.right, root2.left):
                return False
            
        
        if root1 and root2 and root1.val == root2.val:
            return True
        else:
            return False
"""