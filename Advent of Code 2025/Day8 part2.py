import sys
import math


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n  # Track number of disjoint sets

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by size
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            self.count -= 1  # Decrement component count
            return True
        return False


def main():
    try:
        with open('input.txt', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return

    points = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 3:
            try:
                x, y, z = map(int, parts)
                points.append((x, y, z))
            except ValueError:
                continue

    n = len(points)
    if n < 2:
        print(0)
        return

    # Generate all pairs with their squared Euclidean distance
    edges = []
    for i in range(n):
        p1 = points[i]
        for j in range(i + 1, n):
            p2 = points[j]
            dist_sq = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2
            edges.append((dist_sq, i, j))

    # Sort edges by distance (smallest first)
    edges.sort(key=lambda x: x[0])

    uf = UnionFind(n)

    # Iterate through edges until we form a single component
    # This is essentially Kruskal's algorithm finding the MST edge that completes the graph
    for _, u, v in edges:
        if uf.union(u, v):
            # Check if this connection reduced the number of components to 1
            if uf.count == 1:
                p1 = points[u]
                p2 = points[v]
                result = p1[0] * p2[0]
                print(result)
                return


if __name__ == '__main__':
    main()