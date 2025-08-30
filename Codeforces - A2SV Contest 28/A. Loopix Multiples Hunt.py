import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    l,r,k=map(int, input().split())
    n = r - l + 1
    if k==1:
        print(n)
    else:
        maxx=r//k
        if maxx<l:
            print(0)
        else:
            opp=min(r,maxx)-l+1
            print(max(0,opp))