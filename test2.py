from collections import defaultdict

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    hs = list(map(int, input().split()))
    xs = list(map(int, input().split()))

    def check(T):
        coverage = defaultdict(int)
        for x, h in zip(xs, hs):
            r = (h + T - 1) // T
            if r > m:
                continue
            d = m - r
            L, R = x - d, x + d
            coverage[L] += 1
            coverage[R + 1] -= 1

        active = 0
        for key in sorted(coverage.keys()): 
            active += coverage[key]
            if active >= k:
                return True
        return False

    l, r = 1, max(hs)
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)

