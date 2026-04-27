class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def dfs(row, col, visited):
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return True
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or (row, col) in visited:
                return False
            visited.add((row, col))
            street = grid[row][col]
            for dr, dc, exit_dir in connections[street]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited:
                    next_street = grid[nr][nc]
                    entry_dir = opposite[exit_dir]
                    if any(d == entry_dir for _, _, d in connections[next_street]):
                        if dfs(nr, nc, visited):
                            return True
            return False

        connections = {
            1: [(0, 1, 'right'), (0, -1, 'left')],
            2: [(1, 0, 'down'), (-1, 0, 'up')],
            3: [(0, -1, 'left'), (1, 0, 'down')],
            4: [(0, 1, 'right'), (1, 0, 'down')],
            5: [(0, -1, 'left'), (-1, 0, 'up')],
            6: [(0, 1, 'right'), (-1, 0, 'up')]
        }
        opposite = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
        visited = set()
        return dfs(0, 0, visited)