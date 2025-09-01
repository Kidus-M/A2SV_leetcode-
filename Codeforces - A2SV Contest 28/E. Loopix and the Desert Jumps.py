class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        elif self.rank[x] > self.rank[y]:
            self.par[y] = x
        else:
            self.par[y] = x
            self.rank[x] += 1


def solve(arr):
    n = len(arr)

    union_find = UnionFind(n)

    stack = []

    for index in range(n):
        last = stack[-1] if stack else index
        while stack and arr[stack[-1]] > arr[index]:
            union_find.union(stack.pop(), index)
        if arr[last] > arr[index]:
            stack.append(last)
        else:
            stack.append(index)

    stack = []

    for index in range(n - 1, -1, -1):
        last = stack[-1] if stack else index
        while stack and arr[stack[-1]] < arr[index]:
            union_find.union(stack.pop(), index)
        if arr[last] < arr[index]:
            stack.append(last)
        else:
            stack.append(index)
    #  For Every Componet Representative make the max value as there value
    INF = 10 ** 18
    comp_max = [-INF for _ in range(n)]
    for node in range(n):
        root = union_find.find(node)
        comp_max[root] = max(arr[node], comp_max[root])
    ans = [0 for _ in range(n)]
    for node in range(n):
        root = union_find.find(node)
        ans[node] = comp_max[root]
    return ans


test = int(input())

for _ in range(test):
    n = int(input())

    arr = list(map(int, input().split()))

    ans = solve(arr)
    print(*ans)
