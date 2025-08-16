#  index = 0 ---- n - 1
#  target = 0 --- n // 2
n = int(input())
half = n // 2

p_heads = list(map(float, input().split()))
# print(dfs(0, half))
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
#  tail = p[tail] * dp[index + 1][target]
#  head = p[head] * dp[index + 1][target - 1]
#  dp[i][0] = 1

#  base case

dp[0][0] = 1
#  for i n ---- 1
#  for 1 ---- i + 1
#  dp[index - 1][target] = dp[index - 1][target + 1]
for index in range(1, n + 1):
    for target in range(index + 1):
        if target > 0:
            dp[index][target] = p_heads[index - 1] * dp[index - 1][target - 1]
        dp[index][target] += (1 - p_heads[index - 1]) * dp[index - 1][target]

total_pro = 0
for index in range(half + 1, n + 1):
    total_pro += dp[n][index]
print(total_pro)
