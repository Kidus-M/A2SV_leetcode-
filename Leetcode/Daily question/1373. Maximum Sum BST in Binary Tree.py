# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return (True, 0, float('inf'), float('-inf'))

            l_valid, l_sum, l_min, l_max = dfs(node.left)
            r_valid, r_sum, r_min, r_max = dfs(node.right)

            if l_valid and r_valid and l_max < node.val < r_min:
                cur_sum = node.val + l_sum + r_sum
                self.res = max(cur_sum, self.res)
                cur_min = min(l_min, node.val)
                cur_max = max(r_max, node.val)
                return (True, cur_sum, cur_min, cur_max)

            return (False, 0, float('inf'), float('-inf'))

        dfs(root)
        return self.res