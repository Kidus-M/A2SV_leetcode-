class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        pre = [set() for _ in range(numCourses)]

        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            u = q.popleft()
            for v in graph[u]:
                pre[v] |= pre[u] | {u}
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return [u in pre[v] for u, v in queries]