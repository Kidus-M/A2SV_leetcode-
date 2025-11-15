import math

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))

    L=1
    for x in arr:
        L=L*x//math.gcd(L,x)


        if L>10**18:
            break
    ans=sum(1 for x in arr if L%x==0)
    print(ans)