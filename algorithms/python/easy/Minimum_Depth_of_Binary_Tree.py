# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 65594
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        self.count_deepth(root, 1)
        return self.result
            
        
        
    def count_deepth(self, root, deepth):
        if root.left and root.right:
            self.count_deepth(root.left, deepth+1)
            self.count_deepth(root.right, deepth+1)
        elif root.left:
            self.count_deepth(root.left, deepth+1)
        elif root.right:
            self.count_deepth(root.right, deepth+1)
        else:
            if deepth < self.result:
                self.result = deepth