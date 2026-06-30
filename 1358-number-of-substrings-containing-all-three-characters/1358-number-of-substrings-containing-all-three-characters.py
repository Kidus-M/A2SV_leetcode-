class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        a = b = c = -1
        for i, ch in enumerate(s):
            if ch == 'a':
                a = i
            elif ch == 'b':
                b = i
            else:
                c = i
            res += min(a, b, c) + 1
        return res