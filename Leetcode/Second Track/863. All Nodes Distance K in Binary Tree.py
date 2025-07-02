# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        parent = {}

        def build_parent(node, par):
            if node:
                parent[node] = par
                build_parent(node.left, node)
                build_parent(node.right, node)

        build_parent(root, None)

        visited = set()
        queue = deque()
        queue.append((target, 0))
        visited.add(target)
        result = []

        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node.val)
            elif dist < k:
                for neighbor in (node.left, node.right, parent[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))

        return result