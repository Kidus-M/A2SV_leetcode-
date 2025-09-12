class Solution:
    def isThree(self, n: int) -> bool:
        count = 1
        x = n // 2 + 1
        for i in range(1, x):
            if n % i == 0:
                count += 1

        if count == 3:
            return True
        else:
            return False