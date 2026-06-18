class Solution:
    def angleClock(self, h: int, m: int) -> float:
        return 360-A if (A:=max(h*30.0, m*5.5)-min(h*30.0, m*5.5))>180 else A