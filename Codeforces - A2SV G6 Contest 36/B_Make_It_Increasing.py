t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ops = 0
    possible = True

    for i in range(n - 2, -1, -1):
        if a[i + 1] == 0:
            possible = False
            break

        while a[i] >= a[i + 1]:
            a[i] //= 2
            ops += 1
            if a[i] == 0:
                break

        if a[i] >= a[i + 1]:
            possible = False
            break

    print(ops if possible else -1)
