class TrieNode:
    def __init__(self):
        self.children = [None, None]


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted((m, x, i) for i, (x, m) in enumerate(queries))
        root = TrieNode()
        ans = [-1] * len(queries)
        j = 0

        for m, x, i in queries:
            while j < len(nums) and nums[j] <= m:
                node = root
                for k in range(31, -1, -1):
                    bit = (nums[j] >> k) & 1
                    if node.children[bit] is None:
                        node.children[bit] = TrieNode()
                    node = node.children[bit]
                j += 1

            if j == 0:
                continue
            node = root
            max_xor = 0
            for k in range(31, -1, -1):
                bit = (x >> k) & 1
                if node.children[1 - bit]:
                    max_xor |= (1 << k)
                    node = node.children[1 - bit]
                else:
                    node = node.children[bit]
            ans[i] = max_xor

        return ans