class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(num):
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True
        if 8 <= n <= 11:
            return 11

        for x in range(1, 100000):
            s = str(x)
            pal = int(s + s[-2::-1])
            if pal >= n and is_prime(pal):
                return pal
        return -1