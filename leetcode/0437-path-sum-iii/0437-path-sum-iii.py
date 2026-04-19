# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        prefix_sums = {0: 1}
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            
            
            num_paths = prefix_sums.get(curr_sum - targetSum, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
       
            num_paths += dfs(node.left, curr_sum)
            num_paths += dfs(node.right, curr_sum)
            

            prefix_sums[curr_sum] -= 1
            return num_paths

        return dfs(root, 0)
        