t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    a=list(map(int,input().split()))
    tot=sum(a)
    if tot<s:
        print(-1)
        continue
    if tot==s:
        print(0)
        continue
    left=0
    cur=0
    best=-1
    for right in range(n):
        cur+=a[right]
        while cur>s and left<=right:
            cur-=a[left]
            left+=1
        if cur==s:
            best=max(best,right-left+1)
    if best==-1:
        print(-1)
    else:
        print(n-best)
