t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if k>(n-1)//2:
        print(-1)
        continue
    a=list(range(1,n+1))
    for i in range(1,2*k,2):
        a[i],a[i+1]=a[i+1], a[i]
    print(*a)