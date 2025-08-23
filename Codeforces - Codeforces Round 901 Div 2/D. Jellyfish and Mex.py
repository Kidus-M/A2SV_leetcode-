t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=set(a)
    mex=0
    while mex in s:
        mex+=1
    freq={}
    for x in a:
        if x<=mex:
            freq[x]=freq.get(x,0)+1
    ans=mex
    for i in range(mex):
        if freq.get(i,0)>1:
            ans+=freq[i]-1
    print(ans)
