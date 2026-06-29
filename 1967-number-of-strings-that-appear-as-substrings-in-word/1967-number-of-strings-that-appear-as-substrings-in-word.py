class Solution:
    def isSubstring(self, word: str, pat: str) -> bool:
        n = len(word)
        m = len(pat)
        for i in range(n - m + 1):
            j = 0
            while j < m and word[i + j] == pat[j]:
                j += 1

            if j == m:
                return True

        return False

    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0

        for s in patterns:
            if self.isSubstring(word, s):
                count += 1

        return count