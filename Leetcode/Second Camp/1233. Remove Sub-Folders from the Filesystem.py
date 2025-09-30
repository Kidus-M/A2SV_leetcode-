class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        for path in folder:
            node = root
            parts = path.split("/")[1:]
            for p in parts:
                if node.end:
                    break
                if p not in node.children:
                    node.children[p] = TrieNode()
                node = node.children[p]
            node.end = True
        res = []

        def dfs(node, path):
            if node.end:
                res.append("/" + "/".join(path))
                return
            for key, child in node.children.items():
                dfs(child, path + [key])

        dfs(root, [])
        return res