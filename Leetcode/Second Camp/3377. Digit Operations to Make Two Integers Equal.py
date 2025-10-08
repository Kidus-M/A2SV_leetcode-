class Solution:
    def minOperations(self, n: int, m: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

        if len(str(n)) != len(str(m)):
            return -1
        if is_prime(n) or is_prime(m):
            return -1

        pq = [(n, n)]
        dist = {n: n}

        while pq:
            cost, cur = heapq.heappop(pq)
            if cur == m:
                return cost
            if cost > dist[cur]:
                continue
            s = str(cur)
            for i in range(len(s)):
                d = int(s[i])
                for nd in [d + 1, d - 1]:
                    if 0 <= nd <= 9:
                        nxt = int(s[:i] + str(nd) + s[i + 1:])
                        if not is_prime(nxt):
                            new_cost = cost + nxt
                            if nxt not in dist or new_cost < dist[nxt]:
                                dist[nxt] = new_cost
                                heapq.heappush(pq, (new_cost, nxt))
        return -1