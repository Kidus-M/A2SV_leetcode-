class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = defaultdict(list)
        for u, v in hierarchy:
            adj[u].append(v)

        def dfs(u):
            full, half = present[u-1], present[u-1] // 2
            pfull = future[u-1] - full
            phalf = future[u-1] - half
            INF = -10**18

            skip0 = [0] + [INF] * budget
            buy0  = [INF] * (budget+1)
            if full <= budget: buy0[full] = pfull

            skip1 = [0] + [INF] * budget
            buy1  = [INF] * (budget+1)
            if half <= budget: buy1[half] = phalf

            def merge(A, B):
                C = [INF] * (budget+1)
                for ca in range(budget+1):
                    va = A[ca]
                    if va <= INF//2: continue
                    for cb in range(budget+1 - ca):
                        vb = B[cb]
                        if vb <= INF//2: continue
                        C[ca+cb] = max(C[ca+cb], va + vb)
                return C

            for v in adj[u]:
                dp0_v, dp1_v = dfs(v)
                skip0 = merge(skip0, dp0_v)
                buy0  = merge(buy0,  dp1_v)
                skip1 = merge(skip1, dp0_v)
                buy1  = merge(buy1,  dp1_v)

            dp0 = [max(skip0[i], buy0[i]) for i in range(budget+1)]
            dp1 = [max(skip1[i], buy1[i]) for i in range(budget+1)]
            return dp0, dp1

        dp0_root, _ = dfs(1)
        return max(dp0_root)