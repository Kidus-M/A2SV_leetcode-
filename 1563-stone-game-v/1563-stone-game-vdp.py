class Solution:

    def game(self, dp, a, i, j, total):

        if i >= j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        ans = 0
        sum_till_k = 0

        for k in range(i, j):

            sum_till_k += a[k]

            sum_after_k = total - sum_till_k

            if sum_till_k > sum_after_k:

                ans = max(
                    ans,
                    sum_after_k +
                    self.game(
                        dp, a, k + 1, j, sum_after_k
                    )
                )

            elif sum_till_k < sum_after_k:

                ans = max(
                    ans,
                    sum_till_k +
                    self.game(
                        dp, a, i, k, sum_till_k
                    )
                )

            else:

                ans = max(
                    ans,
                    sum_till_k +
                    max(
                        self.game(
                            dp, a, k + 1, j, sum_after_k
                        ),
                        self.game(
                            dp, a, i, k, sum_till_k
                        )
                    )
                )

        dp[i][j] = ans
        return ans

    def stoneGameV(self, stoneValue):

        n = len(stoneValue)

        dp = [[-1] * n for _ in range(n)]

        total_sum = sum(stoneValue)

        return self.game(
            dp, stoneValue, 0, n - 1, total_sum
        )