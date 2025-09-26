class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False


class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                index = ord(char) - ord('a')
                if node.children[index] is None:
                    node.children[index] = TrieNode()
                node = node.children[index]
            node.is_end = True

        result = ""
        stack = [(root, "")]
        while stack:
            node, prefix = stack.pop()
            if len(prefix) > len(result) or (len(prefix) == len(result) and prefix < result):
                if node.is_end:
                    result = prefix
            for i in range(25, -1, -1):
                if node.children[i] and node.children[i].is_end:
                    stack.append((node.children[i], prefix + chr(i + ord('a'))))

        return result