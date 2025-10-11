t=int(input())
for _ in range(t):
    n,m=map(int, input().split())
    a=list(map(int, input().split()))
    a.sort(reverse=True)
    k=min(n,m)
    ans=0
    for i in range(k):
        ans += a[i]*(m-i)
    print(ans)