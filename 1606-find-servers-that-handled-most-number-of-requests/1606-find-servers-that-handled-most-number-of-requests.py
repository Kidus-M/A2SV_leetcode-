class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        n = len(arrival)
        busiests = [0] * k
        idx = SortedList(range(k))
        h = []
        for i, t in enumerate(arrival):
            while h and h[0][0] <= t:
                _, s = heappop(h)
                idx.add(s)
            if len(h) == k:
                continue
            j = idx[idx.bisect_left(i % k)] if i % k <= idx[-1] else idx[0]
            heappush(h, (t + load[i], j))
            busiests[j] += 1
            idx.remove(j)
        m = max(busiests)
        return [i for i in range(k) if busiests[i] == m]