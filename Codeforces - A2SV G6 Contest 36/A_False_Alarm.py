t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    max_closed = 0
    current = 0

    for door in a:
        if door == 1:
            current += 1
            max_closed = max(max_closed, current)
        else:
            current = 0

    if max_closed <= x:
        print("YES")
    else:
        print("NO")
