t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    ugly_indices = []
    current_max = 0

    for i in range(n):
        if p[i] > current_max:
            current_max = p[i]
            ugly_indices.append(i)

    if len(ugly_indices) <= 1:
        print(*p)
        continue

    i = ugly_indices[0]
    j = ugly_indices[-1]
    p[i], p[j] = p[j], p[i]

    print(*p)