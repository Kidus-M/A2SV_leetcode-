class Solution:
    def racecar(self, target: int) -> int:
        q = deque()
        q.append((0, 1, 0))

        while q:
            cp, cs, nm = q.popleft()

            if cp == target:
                return nm

            q.append((cp + cs, cs * 2, nm + 1))

            if (cp + cs > target and cs > 0) or (cp + cs < target and cs < 0):
                if cs < 0:
                    q.append((cp, 1, nm + 1))
                else:
                    q.append((cp, -1, nm + 1))