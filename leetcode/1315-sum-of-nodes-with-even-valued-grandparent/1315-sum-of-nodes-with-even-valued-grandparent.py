# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, parent, grandparent):
            if not node:
                return 0
            sum = 0
            if grandparent and grandparent.val %2 ==0:
                sum += node.val
            sum += dfs(node.left, node, parent)
            sum += dfs(node.right, node, parent)
            return sum
        return dfs(root,None , None)
        