t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    pos = [0] * (n + 1)
    for i in range(n):
        pos[a[i]] = i

    offline = 0
    last = n  # larger than any index

    for i in range(n - 1, -1, -1):
        if pos[b[i]] < last:
            offline += 1
            last = pos[b[i]]
        else:
            break

    print(n - offline)
