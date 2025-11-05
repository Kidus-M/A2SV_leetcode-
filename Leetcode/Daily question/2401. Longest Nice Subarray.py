from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        store = 0
        index = 0
        longest = 1
        for i in range(len(nums)):
            while store & nums[i] != 0:
                store = store ^ nums[index]
                index += 1

            store = store | nums[i]
            longest = max(longest, i - index + 1)
        return longest
