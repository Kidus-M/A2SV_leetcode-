class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.bit_len = 40

    def insert(self, num):
        node = self.root
        for i in range(self.bit_len - 1, -1, -1):
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def query_max_xor(self, num):
        node = self.root
        res = 0
        for i in range(self.bit_len - 1, -1, -1):
            bit = (num >> i) & 1
            opp = 1 - bit
            if node.children[opp]:
                res |= (1 << i)
                node = node.children[opp]
            else:
                node = node.children[bit]
        return res

n = int(input())
a = list(map(int, input().split()))
pref = [0] * (n + 1)
for i in range(1, n + 1):
    pref[i] = pref[i - 1] ^ a[i - 1]
total = pref[n]
trie = Trie()
ans = 0
for x in range(n, -1, -1):
    trie.insert(pref[x])
    T = pref[x] ^ total
    curr_max = trie.query_max_xor(T)
    ans = max(ans, curr_max)
print(ans)