class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.value = 0
        self.is_end = False


class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for char in key:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end = True
        node.value = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                return 0
            node = node.children[index]

        def dfs(node):
            total = node.value if node.is_end else 0
            for child in node.children:
                if child is not None:
                    total += dfs(child)
            return total

        return dfs(node)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)