class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n < 2 * k + 1:
            return []

        non_inc = [1] * n
        non_dec = [1] * n

        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                non_inc[i] = non_inc[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                non_dec[i] = non_dec[i + 1] + 1

        result = []
        for i in range(k, n - k):
            if non_inc[i - 1] >= k and non_dec[i + 1] >= k:
                result.append(i)

        return result