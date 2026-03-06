class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        lengthS = len(s)
        lengthT = len(t)
        
        i = 0
        j = 0
        while i < lengthS and j < lengthT:
            if s[i] == t[j]:
                j += 1
            i += 1
        
        return lengthT - j