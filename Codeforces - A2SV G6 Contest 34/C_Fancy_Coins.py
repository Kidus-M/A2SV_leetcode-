import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m,k,a1,ak=map(int,input().split())
    useRegular=min(a1,m)
    remaining=m-useRegular

    if m<=a1:
        print(0)
    else:
        print((m-a1+k-1)//k)