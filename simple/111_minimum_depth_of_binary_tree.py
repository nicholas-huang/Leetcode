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
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        elif not root.left and root.right:
            return self.minDepth(root.right) + 1
        elif not root.right and root.left:
            return self.minDepth(root.left) + 1
        
        return min(self.minDepth(root.left),self.minDepth(root.right))+1