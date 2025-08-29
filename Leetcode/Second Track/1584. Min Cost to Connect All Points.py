class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))

    def Find(self, x):
        if self.root[x] != x:
            self.root[x] = self.Find(self.root[x])
        return self.root[x]

    def Union(self, x, y):
        x = self.Find(x)
        y = self.Find(y)
        if x == y:
            return
        if y > x:
            self.root[y] = x
        else:
            self.root[x] = y


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))

        edges.sort()

        uf = UnionFind(n)
        total_cost = 0
        edges_used = 0

        for cost, u, v in edges:
            if uf.Find(u) != uf.Find(v):
                uf.Union(u, v)
                total_cost += cost
                edges_used += 1
                if edges_used == n - 1:
                    break

        return total_cost