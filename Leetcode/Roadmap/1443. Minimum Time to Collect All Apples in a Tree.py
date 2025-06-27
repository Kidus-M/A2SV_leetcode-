class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            time = 0
            for child in graph[node]:
                if child == parent:
                    continue
                child_time = dfs(child, node)
                if child_time > 0 or hasApple[child]:
                    time += child_time + 2
            return time

        return dfs(0, -1)