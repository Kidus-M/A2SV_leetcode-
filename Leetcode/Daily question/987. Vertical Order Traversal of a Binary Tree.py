# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(placement, level, root, dic):
            if (not root):
                return
            dic[placement].append((level, root.val))
            helper(placement - 1, level + 1, root.left, dic)
            helper(placement + 1, level + 1, root.right, dic)

        dic = defaultdict(list)
        helper(0, 0, root, dic)
        result = []
        for i in sorted(dic.keys()):
            temp = []
            for j in sorted(dic[i]):
                temp.append(j[1])
            result.append(temp)
        return result

