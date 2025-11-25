class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right < 2:
            return [-1, -1]

        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, right + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False

        prev_prime = -1
        min_diff = float('inf')
        res = [-1, -1]

        for num in range(left, right + 1):
            if is_prime[num]:
                if prev_prime != -1 and num - prev_prime < min_diff:
                    min_diff = num - prev_prime
                    res = [prev_prime, num]
                prev_prime = num

        return res