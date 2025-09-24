class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.words = []


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        for product in sorted(products):
            node = root
            for char in product:
                index = ord(char) - ord('a')
                if node.children[index] is None:
                    node.children[index] = TrieNode()
                node = node.children[index]
                if len(node.words) < 3:
                    node.words.append(product)

        result = []
        node = root
        for char in searchWord:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                result.append([])
                for _ in range(len(searchWord) - len(result)):
                    result.append([])
                break
            node = node.children[index]
            result.append(node.words)

        return result