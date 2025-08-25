class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        ans =0
        while num:
            num &= num -1
            ans += 1

        return ans