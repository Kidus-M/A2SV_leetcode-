import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
q=int(input())

curr=a.copy()

events=[]

for _ in range(q):
    parts=list(map(int,input().split()))
    if parts[0]==1:
        _,i,x=parts
        curr[i-1]=x
    else:
        _,p=parts
        for j in range(n):
            if curr[j] <p:
                curr[j]=p

print(*curr)