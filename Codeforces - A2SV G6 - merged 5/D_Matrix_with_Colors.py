t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))


    pos=[[] for _ in range(k+1)]
    for i , val in enumerate(a):
        pos[val].append(i)

    minge=[n]*(k+2)
    maxge=[-1]*(k+2)


    for i in range(n):
        x=a[i]
        minge[x]=min(minge[x],i)
        maxge[x]=max(maxge[x],i)


    for c in range(k-1,0,-1):
        minge[c]=min(minge[c],minge[c+1])
        maxge[c]=max(maxge[c],maxge[c+1])

    ans=[]
    for c in range(1,k+1):
        if not pos[c]:
            ans.append(0)
            continue

        start=minge[c]
        end=maxge[c]

        side=end-start+1





        ans.append(side+side)

    print(*ans)

