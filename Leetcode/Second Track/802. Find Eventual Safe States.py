class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        state = [0]*n
        def dfs(v):
            if state[v]:
                return state[v] == 2
            state[v] = 1
            for nei in graph[v]:
                if not dfs(nei):
                    return False
            state[v] = 2
            return True
        return [i for i in range(n) if dfs(i)]