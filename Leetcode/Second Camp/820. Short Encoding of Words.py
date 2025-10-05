class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = TrieNode()
        leaves = []
        for word in set(words):
            node = root
            for char in reversed(word):
                index = ord(char) - ord('a')
                if node.children[index] is None:
                    node.children[index] = TrieNode()
                node = node.children[index]
            leaves.append((node, len(word)))

        result = 0
        for node, length in leaves:
            if not any(node.children):
                result += length + 1
        return result