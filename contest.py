t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if k%2==1:
        if n%2==0 or n-k >= 0 and (n-k)%2==0:
            print("YES")
        else:
            print("NO")
    else:
        if n%2==0:
            print("YES")
        else:
            print("NO")
