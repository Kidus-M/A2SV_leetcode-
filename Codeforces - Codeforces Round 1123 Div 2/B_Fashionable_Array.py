t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))

    cnt=[0]*101
    for x in a:
        cnt[x] += 1

    res=[]
    while len(res)<n:
        for v in range(100,0,-1):
            if cnt[v]>0:
                res.append(v)
                cnt[v] -= 1

    print(*res)