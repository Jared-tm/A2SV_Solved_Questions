# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        stack = []
    
        for num in nums:
            new_node = TreeNode(num)
            last_popped = None

            while stack and stack[-1].val < num:
                last_popped = stack.pop()

            new_node.left = last_popped
            if stack:
                stack[-1].right = new_node       
            stack.append(new_node)

        return stack[0]
                