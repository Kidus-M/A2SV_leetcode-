import sys
input=sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    edges = []
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u-= 1
        v-=1
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)

        timer=[0]
        tin=[-1]*n
        low=[-1]*n

        bridges=[]

        def dfs(v,p):
            tin[v]=low[v]=timer[0]

            timer[0]+=1
            for to in graph[v]:
                if to ==p:
                    continue
                if tin[to]!=-1:
                    low[v]=min(low[v],tin[to])
                else:
                    dfs(to,v)
                    low[v]=min(low[v],low[to])
                    if low[to]>tin[v]:
                        bridges.append((v,to))
        dfs(0,-1)

        if not bridges:
            print(n*(n-1)//2)

        visited=[False]*n
        minn = float('inf')

        def dfsS(v,bu,bv):
            visited[v]=True
            size=1
            for to in graph[v]:
                if (v==bu and to ==bv) or (v==bv and to==bu):
                    continue
                if not visited[to]:
                    size += dfsS(to,bu,bv)

            return size

        total=n*(n-1)//2
        for u, v in bridges:
            visited=[False]*n
            sa=dfsS(u,u,v)
            sb=n-sa
            unreachable=sa*sb
            reach=total-unreachable
            minn=min(minn,reach)

        print(minn)
