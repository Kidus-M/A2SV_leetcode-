class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()
        for path in paths:
            node = root
            for p in path:
                if p not in node.children:
                    node.children[p] = TrieNode()
                node = node.children[p]
            node.end = True

        serials = defaultdict(list)

        def dfs(node):
            if not node.children:
                return "()"
            s = "(" + "".join(k + dfs(v) for k, v in sorted(node.children.items())) + ")"
            serials[s].append(node)
            return s

        dfs(root)


        for nodes in serials.values():
            if len(nodes) > 1:
                for n in nodes:
                    n.remove = True
        ans = []

        def collect(node, path):
            for k, v in node.children.items():
                if not getattr(v, "remove", False):
                    ans.append(path + [k])
                    collect(v, path + [k])

        collect(root, [])
        return ans