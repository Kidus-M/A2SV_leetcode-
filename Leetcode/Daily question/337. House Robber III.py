# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(curr):
            if curr is None:
                return 0, 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            rob = curr.val + left[1] + right[1]
            skip = max(left[0], left[1]) + max(right[0], right[1])
            return rob, skip
        return max(dfs(root))