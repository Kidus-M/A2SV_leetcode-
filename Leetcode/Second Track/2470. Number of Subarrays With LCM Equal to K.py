class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            lcm_val = 1

            for j in range(i,n):
                lcm_val = (lcm_val * nums[j]) // math.gcd(lcm_val, nums[j])

                if lcm_val == k:
                    count += 1
                elif lcm_val >= k:
                    break
        return count