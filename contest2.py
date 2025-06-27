from collections import deque
t = int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    dp=[1]*n
    dq=deque()

    for i in range(n):
        while dq and a[i]-a[dq[0]]>k:
            dq.popleft()

        if dq:
            dp[i]=max(dp[i],dp[dq[0]]+1)

        while dq and dp[dq[-1]]<=dp[i]:
            dq.pop()
        dq.append(i)

    print(n-max(dp))