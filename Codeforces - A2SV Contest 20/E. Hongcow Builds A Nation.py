n, m, k = map(int, input().split())
govs = list(map(lambda x: int(x)-1, input().split()))

parent = list(range(n))
size = [1] * n

def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

def union(u, v):
    pu, pv = find(u), find(v)
    if pu != pv:
        parent[pu] = pv
        size[pv] += size[pu]

for _ in range(m):
    u, v = map(int, input().split())
    union(u - 1, v - 1)


comp_map = {}
gov_roots = set()
for i in range(n):
    root = find(i)
    if root not in comp_map:
        comp_map[root] = {
            'size': size[root],
            'gov': False
        }

for g in govs:
    root = find(g)
    comp_map[root]['gov'] = True
    gov_roots.add(root)

max_gov_size = 0
max_gov_root = None
for root in gov_roots:
    if comp_map[root]['size'] > max_gov_size:
        max_gov_size = comp_map[root]['size']
        max_gov_root = root

total_nodes = 0
max_edges = 0

for root, comp in comp_map.items():
    s = comp['size']
    if comp['gov']:
        max_edges += s * (s - 1) // 2
        total_nodes += s
    else:
        # Add its nodes to the largest gov component
        max_edges += s * (s - 1) // 2
        max_edges += s * max_gov_size
        max_gov_size += s
        total_nodes += s

print(max_edges - m)
