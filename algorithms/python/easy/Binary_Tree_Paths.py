# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
对于每一个节点来说，如果有左节点和右节点，那么分开进入
如果只有左节点/右节点，可以进入
如果没有， 那么加入到总的里边

"""
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root == None:
            return []
        
        if root.left == None and root.right == None:
            return [str(root.val)]
        self.result = []
        strings = str(root.val)
        link = "->"
        self.find_path(root, strings, link)
        return self.result
    
    
    def find_path(self, root, strings, link):
        if root.left and root.right:
            strings += link
            self.find_path(root.left, strings+str(root.left.val), link)
            self.find_path(root.right, strings+str(root.right.val), link)

        elif root.left:
            strings += link
            strings += str(root.left.val)
            self.find_path(root.left, strings, link)
        elif root.right:
            strings += link
            strings += str(root.right.val)
            self.find_path(root.right, strings, link)
        else:
            self.result.append(strings)