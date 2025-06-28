t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    found=False
    maxx=n//k
    for y in range(min(100,n//k)):
        remaining=n-k*y
        if  remaining %2==0:
            found=True
            break
    print("YES" if found else "NO")