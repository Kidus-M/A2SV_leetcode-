class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        lps = [0] * len(needle)
        prev_len, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prev_len]:
                prev_len += 1
                lps[i] = prev_len
                i += 1
            else:
                if prev_len != 0:
                    prev_len = lps[prev_len - 1]
                else:
                    lps[i] = 0
                    i += 1
        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == len(needle):
                return i - j
            elif i < len(haystack) and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1