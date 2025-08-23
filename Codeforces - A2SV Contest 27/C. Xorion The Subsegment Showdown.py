t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    z=x^y
    ans=1<<(len(bin(z))) - len(bin(z).rstrip("0"))
    print(ans)