import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    p=min(k-1,n-k+1)
    ans=0
    for i in range(p):
        ans += max(a[i],a[n-1-i])

    if k-1<=n-k+1:
        ans += sum(a[p:n-p])

    print(ans)