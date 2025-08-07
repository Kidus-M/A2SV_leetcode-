class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            prev = 1
            for j in range(1, i):
                temp = dp[j]
                dp[j] = prev + dp[j]
                prev = temp
        return dp