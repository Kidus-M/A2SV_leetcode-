class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        right = 0
        res = 0
        for right in range(len(nums)):
            num = nums[right]
            freq[num] += 1

            while freq[num] > k:
                freq[nums[left]] -= 1
                left += 1
        
            res = max(res, right - left + 1)
        return res