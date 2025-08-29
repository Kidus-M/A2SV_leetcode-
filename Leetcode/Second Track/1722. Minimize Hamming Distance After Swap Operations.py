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
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)

        for a, b in allowedSwaps:
            uf.Union(a, b)

        groups = {}
        for i in range(n):
            root = uf.Find(i)
            if root not in groups:
                groups[root] = [[], []]
            groups[root][0].append(source[i])
            groups[root][1].append(target[i])

        ans = 0
        for root in groups:
            sv = {}
            tv = {}
            for val in groups[root][0]:
                sv[val] = sv.get(val, 0) + 1
            for val in groups[root][1]:
                tv[val] = tv.get(val, 0) + 1

            for val in sv:
                if val not in tv:
                    ans += sv[val]
                else:
                    ans += max(0, sv[val] - tv.get(val, 0))

        return ans