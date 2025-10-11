import sys
input = lambda: sys.stdin.readline().strip()




n, m = map(int, input().split())
cats = list(map(int, input().split()))
graph=[[] for i in range(n+1)]

for _ in range(n-1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans=0
stack=[(1,-1,0)]

while stack:
    node, parent, curr=stack.pop()
    if cats[node-1]==1:
        curr += 1
    else:
        curr=0

    if curr >m:
        continue

    leaf=True

    for n in graph[node]:
        if n != parent:
            leaf=False
            stack.append((n,node,curr))

    if leaf:
        ans += 1

# def dfs(node, parent, curr):
#     global ans
#     if cats[node-1]==1:
#         curr += 1
#     else:
#         curr=0
#
#     if curr >m:
#         return
#
#     leaf=True
#
#     for n in graph[node]:
#         if n != parent:
#             leaf=False
#             dfs(n,node,curr)
#
#     if leaf:
#         ans += 1
# dfs(1,-1,0)
print(ans)



