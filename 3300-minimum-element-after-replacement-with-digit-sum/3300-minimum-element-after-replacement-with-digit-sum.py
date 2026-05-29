class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = []

        for num in nums:
            temp = 0
            for digit in str(num):
                temp += int(digit)

            result.append(temp)

        return min(result)