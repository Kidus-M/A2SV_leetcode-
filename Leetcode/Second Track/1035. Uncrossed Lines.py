class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        memo = [[-1] * (n + 1) for _ in range(m + 1)]

        def helper(i, j):
            if i == m or j == n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if nums1[i] == nums2[j]:
                memo[i][j] = 1 + helper(i + 1, j + 1)
            else:
                memo[i][j] = max(helper(i + 1, j), helper(i, j + 1))
            return memo[i][j]

        return helper(0, 0)