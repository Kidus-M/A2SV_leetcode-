class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        ans = []

        for i in range(n - 2):
            res = []
            for j in range(n - 2):
                k = []
                k.append(grid[i][j])
                k.append(grid[i][j + 1])
                k.append(grid[i][j + 2])
                k.append(grid[i + 1][j])
                k.append(grid[i + 1][j + 1])
                k.append(grid[i + 1][j + 2])
                k.append(grid[i + 2][j])
                k.append(grid[i + 2][j + 1])
                k.append(grid[i + 2][j + 2])
                m = max(k)
                res.append(m)

            ans.append(res)

        return ans