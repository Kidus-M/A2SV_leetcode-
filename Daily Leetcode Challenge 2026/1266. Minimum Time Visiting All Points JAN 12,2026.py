class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res, n = 0, len(points)

        if n == 1:
            return 0
        for i in range(n - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            res += max(abs(x2 - x1), abs(y2 - y1))

        return res