class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        pre = []
        for i in range(n):
            c = 1
            for j in range(n):
                if i == j: continue 
                if items[j][0] % items[i][0] == 0: 
                    c += 1 
            pre.append(items[i] + [c])
        dp = [0] * (budget+1)
        for i in range(n):
            p = pre[i][1]
            cnt = pre[i][2]
            for b in range(p, budget+1):
                dp[b] = max(dp[b], dp[b-p]+1)
            for b in range(budget, p-1, -1):
                dp[b] = max(dp[b], dp[b-p] + cnt)
        return max(dp)