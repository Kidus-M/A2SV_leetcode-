t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    w = s[:k].count('W')
    ans = w

    for i in range(k, n):
        if s[i - k] == 'W':
            w -= 1
        if s[i] == 'W':
            w += 1
        ans = min(ans, w)

    print(ans)
