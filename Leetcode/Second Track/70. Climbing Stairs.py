class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        memo[0]=memo[1]=1
        def helper(n):
            if n not in memo:
                memo[n]=helper(n-1)+helper(n-2)
            return memo[n]
        return helper(n)