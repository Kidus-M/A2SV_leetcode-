t=int(input())
for _ in range(t):
    n,m,k= map(int, input().split())
    if k==n*m-1:
        print("YES")
    else:
        print("NO")