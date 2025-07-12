n=int(input())
p=list(map(int,input().split()))

ans=[]
for s in range(1,n+1):
    visited=set()
    curr=s
    while curr not in visited:
        visited.add(curr)
        curr=p[curr-1]
    ans.append(curr)
print(*ans)