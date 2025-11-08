MOD=998244353

n,k=map(int,input().split())
p=list(map(int,input().split()))

maxx=0
pos=[]

for i in range(n):
    if p[i]>n-k:
        maxx+=p[i]
        pos.append(i)

ways=1
for i in range(1,len(pos)):
    gap=pos[i]-pos[i-1]
    ways=(ways*gap)%MOD

print(maxx,ways)