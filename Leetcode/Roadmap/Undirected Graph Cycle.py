class Solution:
    def isCycle(self, V, edges):
        # Code here
        adj = [[] for _ in range(V)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    states = [0] * V

    def dfs(node, parent):
        states[node] = 1
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if states[neighbor] == 1:
                return True
            if states[neighbor] == 0 and dfs(neighbor, node):
                return True
        states[node] = 2
        return False

    for node in range(V):
        if states[node] == 0 and dfs(node, -1):
            return True

    return False



