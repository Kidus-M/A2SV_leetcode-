class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        if max(nums) == min(nums):return 0
        n = len(nums)
        nums.sort()
        j = 0
        ans = float('inf')
        for i in range(n):
            while nums[i] > nums[j]*k:
                j += 1
            ans = min( ans , n - ( i - j + 1 ))
        return ans