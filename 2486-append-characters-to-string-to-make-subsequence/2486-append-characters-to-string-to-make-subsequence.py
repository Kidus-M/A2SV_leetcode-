class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        lengthS = len(s)
        lengthT = len(t)
        
        Pointer1 = 0
        Pointer2 = 0
        while Pointer1 < lengthS and Pointer2 < lengthT:
            if s[Pointer1] == t[Pointer2]:
                Pointer2 += 1
            Pointer1 += 1
        
        return lengthS - Pointer1