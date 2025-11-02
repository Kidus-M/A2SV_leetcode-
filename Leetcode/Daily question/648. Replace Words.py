class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_root = False


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                index = ord(char) - ord('a')
                if node.children[index] is None:
                    node.children[index] = TrieNode()
                node = node.children[index]
            node.is_root = True

        words = sentence.split()
        result = []
        for word in words:
            node = root
            replacement = []
            for char in word:
                index = ord(char) - ord('a')
                if node.children[index] is None or node.is_root:
                    break
                node = node.children[index]
                replacement.append(char)
            result.append(''.join(replacement) if node.is_root else word)

        return ' '.join(result)