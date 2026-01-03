t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    total_sum = sum(a) + sum(b)
    sq_sum = sum(x * x for x in a) + sum(x * x for x in b)

    dp = {0}

    for i in range(n):
        new_dp = set()
        for s in dp:
            new_dp.add(s + a[i])
            new_dp.add(s + b[i])
        dp = new_dp

    best = float('inf')
    for s in dp:
        best = min(best, s * s + (total_sum - s) * (total_sum - s))

    answer = best + (n - 2) * sq_sum
    print(answer)
