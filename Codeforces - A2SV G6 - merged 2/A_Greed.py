n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

total=sum(a)
b.sort(reverse=True)

if b[0]+b[1]>=total:
    print("YES")
else:
    print("NO")