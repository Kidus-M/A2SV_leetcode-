"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        def dfs(node):
            if not node:
                return 0
            depth = 0
            for child in node.children:
                depth = max(depth, dfs(child))
            return depth + 1

        return dfs(root)
