class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        products = {}
        ans, n = 0, len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                ans += products.get(prod, 0)
                products[prod] = products.get(prod, 0) + 1

        return ans * 8