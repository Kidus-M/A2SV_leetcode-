import sys
input=sys.stdin.readline
t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    pos=[0]*(n+1)
    for i in range(n):
        pos[a[i]]=i%2

    p=pos[n]
    st={(0,0)}
    for v in range(n-1,0,-1):
        c=pos[v]
        nst=set()
        for l,r in st:
            if (p+l+1)%2==c:
                nst.add(((l+1)%2,r))
            if (p+r+1)%2==c:
                nst.add((l,(r+1)%2))
        st=nst
        if not st:
            break

    ok=False
    for l,r in st:
        if l==p:
            ok=True
    print("YES" if ok else "NO")