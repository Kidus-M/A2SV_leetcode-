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
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val
            count = prefix_sums.get(current_sum - targetSum, 0)

            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            prefix_sums[current_sum] -= 1

            return count

        prefix_sums = {0: 1}
        return dfs(root, 0)