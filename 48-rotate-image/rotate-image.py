class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for r in range((n + 1) // 2):
            for c in range(n // 2):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[n - 1 - c][r]
                matrix[n - 1 - c][r] = matrix[n - 1 - r][n - 1 - c]
                matrix[n - 1 - r][n - 1 - c] = matrix[c][n - 1 - r]
                matrix[c][n - 1 - r] = tmp   