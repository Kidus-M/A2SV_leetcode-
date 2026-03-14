t = int(input())
for _ in range(t):
    n, k, p, m = map(int, input().split())
    a = list(map(int, input().split()))

    w = a[p-1]
    d = a[:]
    pos = p
    e = m
    ans = 0

    while e > 0:
        if pos <= k and w <= e:
            e -= w
            ans += 1
            i = pos-1
            x = d.pop(i)
            d.append(x)
            pos = n
            continue

        mn = min(d[:k])
        if mn > e:
            break

        i = 0
        while i < k:
            if d[i] == mn:
                break
            i += 1

        e -= mn
        if i+1 < pos:
            pos -= 1

        x = d.pop(i)
        d.append(x)

    print(ans)