class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count = 0
        n = len(nums)

        for i in range(n):
            curr_gcd = nums[i]
            for j in range(i, n):
                curr_gcd = gcd(curr_gcd, nums[j])
                if curr_gcd == k:
                    count += 1
                if curr_gcd < k:
                    break

        return count