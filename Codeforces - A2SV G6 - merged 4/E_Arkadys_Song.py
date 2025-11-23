from collections import deque
import math
import sys

input=sys.stdin.readline


t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))


    l=[(i-1)%n for i in range(n)]
    r=[(i+1)%n for i in range(n)]

    q=deque()

    for i in range(n):
        if math.gcd(a[i],a[l[i]])==1:
            q.append(i)

    removed=[]
    alive=[True]*n
    while q:
        x=q.popleft()
        if not alive[x]:
            continue
        if math.gcd(a[x],a[l[x]])!=1:
            continue
        alive[x]=False
        removed.append(x+1)

        L=l[x]
        R=r[x]
        
        r[L]=R
        l[R]=L

        if alive[R] and math.gcd(a[L],a[R])==1:
            q.append(R)


    print(len(removed), *removed)