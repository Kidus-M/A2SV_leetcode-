t=int(input())

for _ in range(t):
    n,a,b=map(int,input().split())
    cost=(n//2)*min(2*a,b)+(n%2)*a
    print(cost)