class Solution:
    def minNumberOfSeconds(self, H: int, arr: List[int]) -> int:
        S = sum(arr)
        N = len(arr)
        V = ceil(H / N)
        start, end = 1, V * (V + 1) * max(arr) // 2
        while start < end:
            mid = (start + end) // 2
            W = 0
            for T in arr:
                W += floor(sqrt(2 * mid / T + 0.25) - 0.5)
            if W >= H:
                end = mid
            else:
                start = mid + 1
        return start