class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def dfs(s, start, word_set):
            valid_substr = []

            if start == len(s):
                valid_substr.append("")
            for end in range(start + 1, len(s) + 1):
                prefix = s[start:end]
                if prefix in word_set:
                    sufes = dfs(s, end, word_set)
                    for suf in sufes:
                        valid_substr.append(prefix + ("" if suf == "" else " ") + suf)

            return valid_substr

        word_set = set(wordDict)
        return dfs(s, 0, word_set)