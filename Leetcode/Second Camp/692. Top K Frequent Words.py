class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.freq = 0


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                index = ord(char) - ord('a')
                if node.children[index] is None:
                    node.children[index] = TrieNode()
                node = node.children[index]
            node.freq += 1

        from heapq import heappush, heappop
        heap = []

        def dfs(node, word):
            if node.freq > 0:
                heappush(heap, (-node.freq, word))
            for i in range(26):
                if node.children[i]:
                    dfs(node.children[i], word + chr(i + ord('a')))

        dfs(root, "")
        result = []
        for _ in range(k):
            if heap:
                freq, word = heappop(heap)
                result.append(word)

        return result