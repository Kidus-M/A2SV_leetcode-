n = int(input())
a = [0] * 3
for x in map(int, input().split()):
    a[x-1] += 1

MX = 305
dp = [[[0.0] * MX for _ in range(MX)] for _ in range(MX)]

p = 1.0 / n
for k in range(n + 1):
    for j in range(n + 1):
        for i in range(n + 1):
            z = n - i - j - k
            if z < 0:
                break
            if z == n:
                continue
            x = 1 - z * p
            if i:
                dp[i][j][k] += dp[i-1][j][k] * i * p
            if j:
                dp[i][j][k] += dp[i+1][j-1][k] * j * p
            if k:
                dp[i][j][k] += dp[i][j+1][k-1] * k * p
            dp[i][j][k] += 1
            dp[i][j][k] /= x

print(f"{dp[a[0]][a[1]][a[2]]:.10f}")