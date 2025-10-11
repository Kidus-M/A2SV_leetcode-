t=int(input())
for _ in range(t):
    n,k=map(int, input().split())
    a=list(map(int, input().split()))

    s=sum(a)
    tmax=(s+k)//n

    M=max(a)
    minn = min(a)
    c=a.count(minn)


    if tmax<M:
        print(-1)
        continue

    coins=sum((tmax-x) for x in a if x >minn)
    extra=tmax-minn-1
    if extra >0 and c>1:
        coins += (c-1)*extra

    print(coins)





