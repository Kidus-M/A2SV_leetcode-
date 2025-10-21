class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        r = i = j = 0
        h = Counter()

        for a in nums:
            while j < n and nums[j] <= a + k:
                h[nums[j]] += 1
                j += 1

            while i < n and nums[i] < a - k:
                h[nums[i]] += 1
                i += 1

            c = min(j - i, h[a] + numOperations)
            r = max(r, c)

        i = 0
        for j in range(n):
            while nums[i] + k + k < nums[j]:
                i += 1
            r = max(r, min(j - i + 1, numOperations))

        return r
