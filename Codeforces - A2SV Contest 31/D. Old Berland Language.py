import sys
class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def can_insert(self, s):
        node = self.root
        for i, c in enumerate(s):
            bit = int(c)
            if not node.children[bit]:
                if node.is_end:
                    return False
                node.children[bit] = TrieNode()
            node = node.children[bit]
            if i + 1 == len(s) and (node.is_end or node.children[0] or node.children[1]):
                return False
        return True

    def insert(self, s):
        node = self.root
        for c in s:
            bit = int(c)
            node = node.children[bit]
        node.is_end = True
input=sys.stdin.readline
n = int(input())
lengths = list(map(int, input().split()))
trie = Trie()
words = []
for l in lengths:
    found = False
    for i in range(1 << l):
        s = bin(i)[2:].zfill(l)
        if trie.can_insert(s):
            trie.insert(s)
            words.append(s)
            found = True
            break
    if not found:
        print("NO")
        exit()
print("YES")
for w in words:
    print(w)