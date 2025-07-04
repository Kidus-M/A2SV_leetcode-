# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sum = 0
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.bstToGst(root.right)  # Traverse the right subtree
            self.sum += root.val  # Update the sum
            root.val = self.sum  # Update the current node's value
            self.bstToGst(root.left)  # Traverse the left subtree
        return root