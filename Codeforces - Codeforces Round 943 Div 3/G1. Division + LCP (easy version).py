def z_function(s):
    n = len(s)
    z = [0]*n
    z[0] = n
    l = 0
    r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z

from bisect import bisect_left

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    s = input().strip()
    k = l
    z = z_function(s)

    def possible(x):
        pos = [0]
        for i in range(1, n):
            if z[i] >= x:
                pos.append(i)
        prev = 0
        count = 1
        idx = 0
        while count < k:
            need = prev + x
            idx = bisect_left(pos, need, lo=idx+1)
            if idx >= len(pos):
                return False
            prev = pos[idx]
            count += 1
        return True

    lo, hi = 0, n
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if possible(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(ans)
