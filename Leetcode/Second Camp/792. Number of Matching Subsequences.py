class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.words = []

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = [[] for _ in range(26)]
        for word in words:
            buckets[ord(word[0]) - ord('a')].append(word)
        result = 0
        for char in s:
            index = ord(char) - ord('a')
            curr_words = buckets[index]
            buckets[index] = []
            for word in curr_words:
                if len(word) == 1:
                    result += 1
                else:
                    buckets[ord(word[1]) - ord('a')].append(word[1:])
        return result