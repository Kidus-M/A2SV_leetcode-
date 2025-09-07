import sys
input=sys.stdin.readline
MOD=10**9+7
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    odd=[0]*n
    e=[0]*n
    for i,x in enumerate(a):
        cnt=0
        while x%2==0:
            x//=2
            cnt+=1
        odd[i]=x
        e[i]=cnt
    pref=[0]*(n+1)
    for i in range(n):
        pref[i+1]=pref[i]+odd[i]
    f=[0]*(n+1)
    for i in range(1,n+1):
        best=0
        total_e=0
        for k in range(i,0,-1):
            total_e+=e[k-1]
            if total_e>60:
                break
            s=pref[i]-pref[k-1]
            val=f[k-1]+s+odd[i-1]*((1<<total_e)-1)
            if val>best:
                best=val
        f[i]=best
    print(' '.join(str(x%MOD) for x in f[1:]))
