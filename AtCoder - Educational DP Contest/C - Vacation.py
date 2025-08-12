N = int(input())
activities = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0][0], dp[0][1], dp[0][2] = activities[0]

for i in range(1, N):
    a, b, c = activities[i]
    dp[i][0] = a + max(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = b + max(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = c + max(dp[i - 1][0], dp[i - 1][1])

print(max(dp[N - 1]))