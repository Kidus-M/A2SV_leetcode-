t=int(input())

for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    a.sort(reverse=True)
    result=sum(a[:k+1])

    print(result)