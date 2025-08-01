class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices) // 3
        memo1 = [[-1] * (n + 1) for _ in range(len(slices) + 1)]
        memo2 = [[-1] * (n + 1) for _ in range(len(slices))]

        def helper(arr, i, count, end, memo):
            if count == 0:
                return 0
            if i >= end:
                return float('-inf')
            if memo[i][count] != -1:
                return memo[i][count]
            take = arr[i] + helper(arr, i + 2, count - 1, end, memo)
            skip = helper(arr, i + 1, count, end, memo)
            memo[i][count] = max(take, skip)
            return memo[i][count]

        case1 = helper(slices, 0, n, len(slices) - 1, memo1)
        case2 = helper(slices, 1, n, len(slices), memo2)
        return max(case1, case2)