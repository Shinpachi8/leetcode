# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False

        self.sum = sum
        self.result_value = []
        result = root.val
        if root.left == None and root.right == None:
            if result == self.sum:
                return True
            else:
                return False
        self.do_sum(root, result)
        if self.result_value:
            return True
        else:
            return False
        
    
    
    def do_sum(self, root, result):
        if root.left and root.right:
            #if result + root.left.val <= self.sum:
            self.do_sum(root.left, result+root.left.val)

        #elif result + root.right.val <= self.sum:
            self.do_sum(root.right, result+root.right.val)

            # else:
            #     return False
        elif root.left:
            self.do_sum(root.left, result+root.left.val)

        elif root.right:

            self.do_sum(root.right, result+root.right.val)
 

        else:
            if result == self.sum:
                self.result_value.append(1)