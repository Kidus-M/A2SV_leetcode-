class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        mp = Counter(nums)
        ans = 0
        for num, freq in sorted(mp.items()):
            count = 0
            x = num
            if x == 1:
                count = mp[1]
                if count % 2 == 0:
                    count -= 1
                ans = max(ans, count)
                continue

            while x in mp and mp[x]:
                if mp[x] >= 2:
                    count += 2
                else:
                    count += 1
                    break
                if x > 10**6:
                    break
                x *= x

            if count % 2 == 0:
                count -= 1
            ans = max(ans, count)

        return ans
