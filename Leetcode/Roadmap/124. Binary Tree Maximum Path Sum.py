# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(node):
            if not node:
                return 0
            leftMaxPath = max(dfs(node.left), 0)
            rightMaxPath = max(dfs(node.right), 0)
            maxIfNodeIsRoot = node.val + leftMaxPath + rightMaxPath
            self.maxSum = max(self.maxSum, maxIfNodeIsRoot)
            return node.val + max(leftMaxPath, rightMaxPath)

        self.maxSum = float('-inf')
        dfs(root)
        return self.maxSum