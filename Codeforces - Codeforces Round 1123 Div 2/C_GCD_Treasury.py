import sys
from math import gcd
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    sm={}
    for v in a:
        h=gcd(v,x)
        if h>1:
            sm[h]=sm.get(h,0)+v
    hs=list(sm)

    reach={x}
    st=[x]
    while st:
        d=st.pop()
        for h in hs:
            g=gcd(h,d)
            if g>1 and g not in reach:
                reach.add(g)
                st.append(g)
    ans=0
    for d in reach:
        s=0
        for h in hs:
            if h%d==0:
                s += sm[h]
        ans=max(ans,s)

    print(ans)