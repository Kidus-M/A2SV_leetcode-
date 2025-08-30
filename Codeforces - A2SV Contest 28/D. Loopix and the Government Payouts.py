import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
q=int(input())

events=[]

for _ in range(q):
    parts=list(map(int,input().split()))
    if parts[0]==1:
        _,i,x=parts
        events.append((1,i-1,x))
    else:
        _,p=parts
        events.append((2,p))

ans=[None]*n
maxx=0

for ev in reversed(events):
    if ev[0]==2:
        _,p=ev
        maxx=max(maxx,p)
    else:
        _, i, x = ev
        if ans[i] is None:
            ans[i]=max(x,maxx)


for i in range(n):
    if ans[i] is None:
        ans[i]=max(a[i],maxx)

print(*ans)