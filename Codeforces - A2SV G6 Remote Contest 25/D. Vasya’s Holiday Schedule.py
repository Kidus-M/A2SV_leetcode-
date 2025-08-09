n=int(input())
a=list(map(int, input().split()))

inf=float('inf')
dp=[[inf]*3 for _ in range(n)]

dp[0][0]=1

if a[0] in (1,3):
    dp[0][1]=0
if a[0] in (2,3):
    dp[0][2]=0

for i in range(1,n):
    dp[i][0]=1+min(dp[i-1])

    if a[i] in(1,3):
        dp[i][1]=min(dp[i-1][0],dp[i-1][2])

    if a[i] in (2,3):
        dp[i][2]=min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1]))