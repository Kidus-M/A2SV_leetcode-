import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n,T=map(int,input().split())
    a=list(map(int,input().split()))
    S=sum(a)
    target=min(T,S-T)

    colors=[0]*n
    count={}
    for i in range(n):
        x=a[i]
        if T %2==0 and x==T//2:
            colors[i]=count.get(x,0)%2
            count[x]=count.get(x,0)+1
        else:
            if x *2<T:
                colors[i]=0
            else:
                colors[i]=1

    print(*colors)