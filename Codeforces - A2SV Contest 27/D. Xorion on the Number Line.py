import bisect
t=int(input())
for _ in range(t):
    n,k,q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a=[0]+a
    b=[0]+b
    res=[]
    for _ in range(q):
        d=int(input())
        i=bisect.bisect_left(a,d)
        if a[i]==d:
            res.append(b[i])
            continue
        else:
            j=i-1
            ans=b[j]+(d-a[j])*(b[i]-b[j])//(a[i]-a[j])
            res.append(int(ans))
    print(*res)
