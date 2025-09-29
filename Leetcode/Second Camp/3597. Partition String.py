class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end


class Solution:
    def partitionString(self, s: str) -> List[str]:
        trie = Trie()
        res = []
        cur = ""

        for ch in s:
            cur += ch
            if not trie.search(cur):
                res.append(cur)
                trie.insert(cur)
                cur = ""

        return res