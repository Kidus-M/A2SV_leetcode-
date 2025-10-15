class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        intr_arr = []
        cnt = 1
        for i in range(len(nums) - 1):

            if (nums[i] < nums[i + 1]):
                cnt += 1
            else:
                intr_arr.append(cnt)
                cnt = 1

        intr_arr.append(cnt)

        maxx = intr_arr[0] // 2

        for i in range(1, len(intr_arr)):

            r1 = min(intr_arr[i - 1], intr_arr[i])
            r2 = intr_arr[i] // 2
            r = max(r1, r2)

            if (r > maxx):
                maxx = r

        return maxx