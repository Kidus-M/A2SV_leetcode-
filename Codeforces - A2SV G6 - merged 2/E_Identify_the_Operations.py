import sys
input=sys.stdin.readline
t=int(input())
MOD=998244353
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))


    posa=[0]*(n+1)
    for i, val in enumerate(a):
        posa[val]=i

    bset=set(b)
    ans=1

    for val in b:
        pos=posa[val]
        leftok=(pos>0 and a[pos-1] not in bset)
        rightok=(pos<n-1 and a[pos+1] not in bset)
        if leftok and rightok:
            ans=(ans*2)%MOD
        elif not leftok and not rightok:
            ans=0
            break
        bset.remove(val)
    print(ans)