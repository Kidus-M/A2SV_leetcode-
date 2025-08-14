INF = float('inf')
N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
max_value_sum = sum(v for _, v in items)
dp = [INF] * (max_value_sum + 1)
dp[0] = 0
for w, v in items:
    for val in range(max_value_sum, v - 1, -1):
        dp[val] = min(dp[val], dp[val - v] + w)
ans = 0
for val in range(max_value_sum + 1):
    if dp[val] <= W:
        ans = val
print(ans)
