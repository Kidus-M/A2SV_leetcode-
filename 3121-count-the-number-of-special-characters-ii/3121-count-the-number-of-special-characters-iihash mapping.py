class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mp = {}

        for i,ch in enumerate(word):
            if ch not in mp:
                mp[ch] = []
            mp[ch].append(i)

        res = 0

        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)

            if lower not in mp or upper not in mp:
                continue

            loweridx = mp[lower][-1]
            upperidx = mp[upper][0]

            if loweridx < upperidx:
                res += 1

        return res