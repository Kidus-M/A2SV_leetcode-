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
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        result = []

        for u, v in requests:
            valid = True
            ru, rv = uf.Find(u), uf.Find(v)

            for x, y in restrictions:
                rx, ry = uf.Find(x), uf.Find(y)
                if (ru == rx and rv == ry) or (ru == ry and rv == rx):
                    valid = False
                    break

            result.append(valid)
            if valid:
                uf.Union(u, v)

        return result