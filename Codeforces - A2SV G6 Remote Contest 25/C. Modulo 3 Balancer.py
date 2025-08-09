t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))


    c=[0,0,0]
    for i in a:
        c[i%3]+=1


    target=n // 3
    ans=0

    while min(c)!= target:
        for i in range(3):
            if c[i]>target:
                e=c[i]-target
                c[i]-=e
                c[(i+1)%3]+=e
                ans += e

    print(ans)