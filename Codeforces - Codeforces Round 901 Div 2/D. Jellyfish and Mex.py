
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))


    counts = [0] * (n + 1)
    for x in a:
        if x <= n:
            counts[x] += 1


    initial_mex = 0
    while initial_mex < len(counts) and counts[initial_mex] > 0:
        initial_mex += 1

    if initial_mex == 0:
        print(0)
        continue


    dp = [0] * (initial_mex + 1)
    infinity = float('inf')

    for i in range(1, initial_mex + 1):
        dp[i] = infinity
        for j in range(i):
            cost = dp[j] + (counts[j] - 1) * i + j
            dp[i] = min(dp[i], cost)

    print(dp[initial_mex])

