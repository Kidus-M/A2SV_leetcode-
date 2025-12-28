import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt_b = {}
    for x in b:
        cnt_b[x] = cnt_b.get(x, 0) + 1
    cnt_w = {}
    matches = 0
    ans = 0
    for i in range(m):
        x = a[i]
        if x in cnt_b:
            cnt_w[x] = cnt_w.get(x, 0) + 1
            if cnt_w[x] <= cnt_b[x]:
                matches += 1

    if matches >= k:
        ans += 1
    for i in range(m, n):
        add = a[i]
        rem = a[i - m]

        if add in cnt_b:
            cnt_w[add] = cnt_w.get(add, 0) + 1
            if cnt_w[add] <= cnt_b[add]:
                matches += 1

        if rem in cnt_b:
            if cnt_w[rem] <= cnt_b[rem]:
                matches -= 1
            cnt_w[rem] -= 1

        if matches >= k:
            ans += 1
    print(ans)
