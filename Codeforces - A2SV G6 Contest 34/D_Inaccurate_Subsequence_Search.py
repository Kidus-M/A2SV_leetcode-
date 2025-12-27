import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt_b = defaultdict(int)
    for x in b:
        cnt_b[x] += 1

    cnt_w = defaultdict(int)
    matches = 0
    ans = 0

    for i in range(m):
        x = a[i]
        cnt_w[x] += 1
        if cnt_w[x] <= cnt_b[x]:
            matches += 1

    if matches >= k:
        ans += 1

    for i in range(m, n):
        add = a[i]
        rem = a[i - m]

        cnt_w[add] += 1
        if cnt_w[add] <= cnt_b[add]:
            matches += 1

        if cnt_w[rem] <= cnt_b[rem]:
            matches -= 1
        cnt_w[rem] -= 1

        if matches >= k:
            ans += 1

    print(ans)
