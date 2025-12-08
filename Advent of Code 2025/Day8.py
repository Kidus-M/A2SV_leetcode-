import sys
import math


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

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
    # We use squared distance to avoid sqrt and float precision issues during sorting
    edges = []
    for i in range(n):
        p1 = points[i]
        for j in range(i + 1, n):
            p2 = points[j]
            dist_sq = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2
            edges.append((dist_sq, i, j))

    # Sort edges by distance (smallest first)
    edges.sort(key=lambda x: x[0])

    # Connect the top 1000 pairs
    uf = UnionFind(n)
    limit = min(len(edges), 1000)

    for k in range(limit):
        _, u, v = edges[k]
        uf.union(u, v)

    # Collect component sizes
    # We only care about the sizes of the roots
    component_sizes = []
    for i in range(n):
        if uf.parent[i] == i:
            component_sizes.append(uf.size[i])

    # Sort sizes descending
    component_sizes.sort(reverse=True)

    # Multiply the 3 largest
    if len(component_sizes) >= 3:
        result = component_sizes[0] * component_sizes[1] * component_sizes[2]
        print(result)
    else:
        # Fallback if fewer than 3 circuits exist (unlikely given the problem)
        result = 1
        for s in component_sizes:
            result *= s
        print(result)


if __name__ == '__main__':
    main()