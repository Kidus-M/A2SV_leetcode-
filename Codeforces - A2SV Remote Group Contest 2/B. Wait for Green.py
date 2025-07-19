t = int(input())
for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()
    if c == 'g':
        print(0)
        continue
    dist = [0] * n
    last_g = -1
    for i in range(2 * n - 1, -1, -1):
        if s[i % n] == 'g':
            last_g = i % n
        if last_g != -1:
            dist[i % n] = (last_g - i % n + n) % n
    max_wait = 0
    for i in range(n):
        if s[i] == c and dist[i] > 0:
            max_wait = max(max_wait, dist[i])
    print(max_wait)