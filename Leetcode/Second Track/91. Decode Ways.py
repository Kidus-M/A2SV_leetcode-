class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [-1] * (n + 1)

        def helper(i):
            if i == n:
                return 1
            if i > n or s[i] == '0':
                return 0
            if memo[i] != -1:
                return memo[i]
            ways = helper(i + 1)
            if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
                ways += helper(i + 2)
            memo[i] = ways
            return memo[i]

        return helper(0)