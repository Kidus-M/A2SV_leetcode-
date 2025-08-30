t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))


    ans=[0]*n
    visited=[False]*n

    for i in range(n):
        if not visited[i]:
            cycle=[]
            x=i
            while not visited[x]:
                visited[x]=True
                cycle.append(x)
                x=p[x]-1
            lenn=len(cycle)
            for v in cycle:
                ans[v]=lenn
    print(*ans)