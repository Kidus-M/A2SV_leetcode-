import bisect
t=int(input())
for _ in range(t):
    n,k,q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a=[0]+a+[n]
    b=[0]+b+[k]

    print(a)
    print(b)





    for _ in range(q):
        d=int(input())
        # i=bisect.bisect_right(a,d)
        # ans=b[i]+ (b[i+1]-b[i]) *d // (a[i+1]-a[i])
        # print(ans)

