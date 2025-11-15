MOD=1000000007
t,k=map(int,input().split())

maxn=100000

dp=[0]*(maxn+1)
pre=[0]*(maxn+1)

dp[0]=1
for i in range(1,maxn+1):
    dp[i]=dp[i-1]
    if i >=k:
        dp[i]=(dp[i]+dp[i-k])%MOD

for i in range(1,maxn+1):
    pre[i]=(pre[i-1]+dp[i])%MOD

for _ in range(t):
    a,b=map(int,input().split())
    ans=(pre[b]-pre[a-1])%MOD
    print(ans)