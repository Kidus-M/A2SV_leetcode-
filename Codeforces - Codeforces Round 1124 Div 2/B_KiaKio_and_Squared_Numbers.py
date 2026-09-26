t=int(input())
cyc=[4,16,37,58,89,145,42,20]
pos={v:i for i,v in enumerate(cyc)}

for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    cnt={}

    for x in a:
        steps=0

        while x!=1 and x not in pos:
            x=sum(int(d)**2 for d in str(x))
            steps += 1

        if x==1:
            key=-1
        else:
            key=(pos[x]-steps)%8

        cnt[key]=cnt.get(key,0)+1

    ans=0
    for v in cnt.values():
        ans += v*(v-1)//2

    print(ans)