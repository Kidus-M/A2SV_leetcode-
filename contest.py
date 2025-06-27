n=int(input())
ratings=list(map(int,input().split()))



idxrating=[(rating,idx) for idx,rating in enumerate(ratings)]
idxrating.sort(reverse=True)


ranks=[0]*n
curr=1

for i in range(n):
    if i>0 and idxrating[i][0]!=idxrating[i-1][0]:
        curr=i+1
    ranks[idxrating[i][1]]=curr

print(*ranks)