class TrieNode:
    def __init__(self):
        self.children = {}
        self.indices = set()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, idx):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.indices.add(idx)

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        trie = Trie()

        for i, word in enumerate(arr):
            L = len(word)
            for start in range(L):
                node = trie.root
                for end in range(start, L):
                    ch = word[end]
                    if ch not in node.children:
                        node.children[ch] = TrieNode()
                    node = node.children[ch]
                    node.indices.add(i)

        res = []
        for i, word in enumerate(arr):
            L = len(word)
            candidate = None
            for length in range(1, L + 1):
                subs = [word[j:j + length] for j in range(L - length + 1)]
                subs.sort()
                for sub in subs:
                    node = trie.search(sub)
                    if node and node.indices == {i}:
                        candidate = sub
                        break
                if candidate:
                    break
            res.append(candidate if candidate else "")

        return res
