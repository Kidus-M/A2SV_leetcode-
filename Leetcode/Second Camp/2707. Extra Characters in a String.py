class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                index = ord(char) - ord('a')
                if node.children[index] is None:
                    node.children[index] = TrieNode()
                node = node.children[index]
            node.is_end = True

        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] != float('inf'):
                node = root
                j = i
                while j < n and node.children[ord(s[j]) - ord('a')]:
                    node = node.children[ord(s[j]) - ord('a')]
                    j += 1
                    if node.is_end:
                        dp[j] = min(dp[j], dp[i] + j - i - (j - i))
                dp[i + 1] = min(dp[i + 1], dp[i] + 1)
        return dp[n]