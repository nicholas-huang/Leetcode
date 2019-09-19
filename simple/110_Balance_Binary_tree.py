# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def ad_depth(root):
            if not root:
                return 0
            left = ad_depth(root.left)
            if left == -1: return -1
            right = ad_depth(root.right)
            if right == -1: return -1
            return max(left,right)+1 if abs(left-right)<2 else -1
        
        if not root:
            return True
        return ad_depth(root) != -1