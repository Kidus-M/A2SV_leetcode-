class Solution:
    def minOperations(self, s: str) -> int:
        countForAlternate0 = 0
        countForAlternate1 = 0

        for i, char in enumerate(s):
            if i % 2 == 0:
                if char == '0':
                    countForAlternate1 += 1
                else:
                    countForAlternate0 += 1
            else:
                if char == '1':
                    countForAlternate1 += 1
                else:
                    countForAlternate0 += 1

        return min(countForAlternate0, countForAlternate1)
