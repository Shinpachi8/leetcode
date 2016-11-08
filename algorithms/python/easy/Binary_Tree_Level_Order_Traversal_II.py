# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
和一的解法一样，只不过结果反过来了。....
这很尴尬呀。回头再试试看。

"""
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        self.result = []
        self.result.append([root.val])
        self.get_result(root,1)
        return self.result[::-1]
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
            