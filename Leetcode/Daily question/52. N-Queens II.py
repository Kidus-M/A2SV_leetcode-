class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self.arr = [-1] * n
        self.helper(0, n)
        return self.count

    def helper(self, row, n):
        if row == n:
            self.count += 1
            return
        for col in range(n):
            if self.isSafe(row, col):
                self.arr[row] = col
                self.helper(row + 1, n)

    def isSafe(self, row, col):
        for i in range(row):
            if self.arr[i] == col or abs(row - i) == abs(col - self.arr[i]):
                return False
        return True