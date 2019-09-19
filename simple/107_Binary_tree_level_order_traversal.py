# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [root]
        result = []
        while q:
            res = []
            next_q = []
            for point in q:
                res.append(point.val)
                if point.left:
                    next_q.append(point.left)
                if point.right:
                    next_q.append(point.right)
            q = next_q
            result.append(res)
        result.reverse()
        return result