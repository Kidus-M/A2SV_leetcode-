class Solution:
    def fib(self, n: int) -> int:
        memo={}
        memo[0]=0
        memo[1]=1
        def fibb(n):
            if n not in memo:
                memo[n]=fibb(n-2)+fibb(n-1)
            return memo[n]

        return fibb(n)