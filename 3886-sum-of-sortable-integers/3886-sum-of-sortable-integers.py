class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        divisors = []
        for i in range(1, isqrt(n) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)

        def isValid(k):
            prev_max = float("-inf")
            for l in range(0, n, k):
                block = nums[l : l + k]

                descents = 0
                descents = sum(block[i] > block[(i + 1) % k] for i in range(k))
                if descents > 1:
                    return False

                curr_min = min(block)
                if curr_min < prev_max:
                    return False

                prev_max = max(block)
            return True

        return sum(div for div in divisors if isValid(div))
