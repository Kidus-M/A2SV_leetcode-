import sys
from bisect import bisect_left
input=sys.stdin.readline

def step(a,n):
    r=n+2*n
    ans=0
    for b in range(29,-1,-1):
        c=0
        for v in a:
            lo=((v>>b)^(ans>>b))<<b
            c += bisect_left(a,lo+(1<<b))-bisect_left(a,lo)
        if c<r:
            r -= c
            ans |= 1<<b

    res=[]
    for i in range(n):
        v=a[i]
        for b in range(29,-1,-1):
            if ans>>b&1:
                lo=(((ans>>b)^1)^(v>>b))<<b
                l=max(bisect_left(a,lo),i+1)
                h=bisect_left(a,lo+(1<<b))
                for j in range(l,h):
                    res.append(v^a[j])
    while len(res)<n:
        res.append(ans)
    res.sort()
    return res

t=int(input())
out=[]
for _ in range(t):
    n,q=map(int,input().split())
    a=sorted(map(int,input().split()))

    d=[a[-1]-a[0]]
    while True:
        b=step(a,n)
        if b==a:
            break
        a=b
        d.append(a[-1]-a[0])

    for _ in range(q):
        x=int(input())
        out.append(d[min(x,len(d)-1)])

print("\n".join(map(str,out)))