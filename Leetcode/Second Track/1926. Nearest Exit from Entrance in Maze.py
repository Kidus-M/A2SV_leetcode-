class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        q = deque([(entrance[0], entrance[1], 0)])

        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            x, y, d = q.popleft()
            if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and [x, y] != entrance:
                return d
            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    maze[nx][ny] = '+'
                    q.append((nx, ny, d + 1))
        return -1