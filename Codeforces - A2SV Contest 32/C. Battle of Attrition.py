import sys
import heapq
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    p = list(map(int, input().split()))

    m=sorted(zip(h,p))
    pre=[0] * n
    pre[-1]=m[-1][1]

    for i in range((n-2),-1,-1):
        pre[i]=min(pre[i+1],m[i][1])

    total=0
    i=0
    while i<n and k >0:
        total += k
        while i<n and m[i][0]<= total:
            i+=1
        if i==n:
            break
        k-=pre[i]

    print("YES" if i==n else "NO")

