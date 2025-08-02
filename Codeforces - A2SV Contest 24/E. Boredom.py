import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()

n=int(input())
a=list(map(int, input().split()))

count=defaultdict(int)
maxx=0
for num in a:
    count[num] += 1
    maxx=max(maxx,num)

dp=[0] *(maxx+2)
dp[1]=count[1]

for i in range(2,maxx+1):
    dp[i]=max(dp[i-1],dp[i-2]+count[i]*i)


print(dp[maxx])


