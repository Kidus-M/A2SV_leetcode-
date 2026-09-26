import sys
input=sys.stdin.readline

t=int(input())
out=[]
for _ in range(t):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))

    ev=[bin(v).count("1")%2==0 for v in a]
    cnt=sum(ev)

    res=[cnt]
    for _ in range(q):
        p,x=map(int,input().split())
        p -= 1
        cnt -= ev[p]
        ev[p]=bin(x).count("1")%2==0
        cnt += ev[p]
        res.append(cnt)

    out.append(" ".join(map(str,res)))

print("\n".join(out))