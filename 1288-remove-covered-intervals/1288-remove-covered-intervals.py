class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x : (x[0], -x[1]))
        ans = 1
        prevA, prevB = intervals[0]

        for i in range(1, len(intervals)):
            a, b = intervals[i]
            
            if prevA <= a and prevB >= b:
                continue
            else:
                ans += 1
                prevA, prevB = a, b

        
        return ans
            



