class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trailing_zeros = []
        for row in grid:
            tz = 0
            j = n - 1
            while j >= 0 and row[j] == 0:
                tz += 1
                j -= 1
            trailing_zeros.append(tz)

        swaps = 0
        for i in range(n):
            need = n - 1 - i
            j = i
            while j < n and trailing_zeros[j] < need:
                j += 1

            if j == n:
                return -1 
            swaps += (j - i)
            while j > i:
                trailing_zeros[j], trailing_zeros[j - 1] = trailing_zeros[j - 1], trailing_zeros[j]
                j -= 1

        return swaps