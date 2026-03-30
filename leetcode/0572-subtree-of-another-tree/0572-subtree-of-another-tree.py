class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not root: 
            return False
        if self.equal(root, subRoot): 
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def equal(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2 or root1.val != root2.val:
            return False
            
        return self.equal(root1.left, root2.left) and self.equal(root1.right, root2.right)