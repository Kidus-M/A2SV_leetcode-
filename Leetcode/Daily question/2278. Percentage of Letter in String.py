class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        l = len(s)
        s = Counter(s)
        return int(s[letter] / l * 100)