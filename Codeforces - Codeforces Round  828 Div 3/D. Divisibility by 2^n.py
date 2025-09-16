import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for x in a:
        while x % 2 == 0:
            cnt += 1
            x //= 2
    if cnt >= n:
        print(0)
        continue
    vals = []
    for i in range(1, n + 1):
        c = 0
        x = i
        while x % 2 == 0:
            c += 1
            x //= 2
        vals.append(c)
    vals.sort(reverse=True)
    ans = 0
    for v in vals:
        if cnt >= n:
            break
        cnt += v
        ans += 1
    print(ans if cnt >= n else -1)