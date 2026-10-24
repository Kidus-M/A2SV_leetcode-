class Solution:
    def countDaysTogether(self, x: str, y: str, z: str, w: str) -> int:
        days=list(accumulate([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], initial=0))
        def cntDays(s):
            return days[(int(s[:2]))-1]+int(s[3:])
        return max(0, min(cntDays(w), cntDays(y))-max(cntDays(z), cntDays(x))+1)
        