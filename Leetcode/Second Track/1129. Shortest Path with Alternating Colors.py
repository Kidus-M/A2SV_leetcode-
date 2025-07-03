class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        graph = [defaultdict(list) for _ in range(2)]
        for u, v in redEdges:
            graph[0][u].append(v)
        for u, v in blueEdges:
            graph[1][u].append(v)

        answer = [-1] * n
        queue = deque()
        visited = set()

        queue.append((0, 0, -1))
        visited.add((0, -1))

        while queue:
            node, dist, last_color = queue.popleft()
            if answer[node] == -1:
                answer[node] = dist

            for next_color in [0, 1]:
                if next_color != last_color:
                    for neighbor in graph[next_color][node]:
                        if (neighbor, next_color) not in visited:
                            visited.add((neighbor, next_color))
                            queue.append((neighbor, dist + 1, next_color))

        return answer