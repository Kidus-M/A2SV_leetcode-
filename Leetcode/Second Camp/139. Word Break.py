class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            node = root
            for char in word:
                index = ord(char) - ord('a')
                if node.children[index] is None:
                    node.children[index] = TrieNode()
                node = node.children[index]
            node.is_end = True

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            if dp[i]:
                node = root
                j = i
                while j < n and node.children[ord(s[j]) - ord('a')]:
                    node = node.children[ord(s[j]) - ord('a')]
                    j += 1
                    if node.is_end:
                        dp[j] = True
                if dp[n]:
                    return True
        return dp[n]