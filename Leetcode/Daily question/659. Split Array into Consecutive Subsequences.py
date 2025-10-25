class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        pq = []

        for k, v in mp.items():
            heapq.heappush(pq, k)


        while pq:
            minn = pq[0]
            count = 0
            while True:
                if minn not in mp:
                    if count < 3:
                        return False
                    break
                mp[minn] -= 1
                count += 1
                if mp[minn] == 0:
                    if minn != pq[0]:
                        return False
                    heapq.heappop(pq)
                if minn + 1 in mp and (mp[minn] >= mp[minn + 1]):
                    if count < 3:
                        return False
                    break

                minn += 1
        return True