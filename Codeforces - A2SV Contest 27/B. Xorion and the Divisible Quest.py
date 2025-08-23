import math
n=int(input())
a=list(map(int,input().split()))
g=a[0]
for i in a:
    g=math.gcd(g,i)
if g in a:
    print(g)
else:
    print(-1)