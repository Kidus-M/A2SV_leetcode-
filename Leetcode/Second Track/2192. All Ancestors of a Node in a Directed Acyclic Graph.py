class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = [[] for _ in range(n)]
        inDeg = [0] * n

        for e in edges:
            graph[e[0]].append(e[1])
            inDeg[e[1]] += 1

        q = deque()
        for i in range(n):
            if inDeg[i] == 0:
                q.append(i)

        ancestors = [set() for _ in range(n)]

        while q:
            u = q.popleft()
            for v in graph[u]:
                inDeg[v] -= 1
                ancestors[v].add(u)
                ancestors[v].update(ancestors[u])
                if inDeg[v] == 0:
                    q.append(v)

        ans = [[] for _ in range(n)]
        for i in range(n):
            ans[i] = sorted(list(ancestors[i]))

        return ans