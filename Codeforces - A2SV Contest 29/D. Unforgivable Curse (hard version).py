import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input().strip()
    t_=input().strip()
    adj=[[] for _ in range(n)]
    for i in range(n):
        if i+k<n:
            adj[i].append(i+k)
            adj[i+k].append(i)
        if i+k+1<n:
            adj[i].append(i+k+1)
            adj[i+k+1].append(i)
    vis=[0]*n
    ok=True
    for i in range(n):
        if not vis[i]:
            q=[i]
            vis[i]=1
            comp=[]
            while q:
                u=q.pop()
                comp.append(u)
                for v in adj[u]:
                    if not vis[v]:
                        vis[v]=1
                        q.append(v)
            chars1=[s[x] for x in comp]
            chars2=[t_[x] for x in comp]
            if sorted(chars1)!=sorted(chars2):
                ok=False
                break
    print("YES" if ok else "NO")
