t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    closed = [i for i in range(n) if a[i] == 1]

    first = closed[0]
    last = closed[-1]

    if last - first + 1 <= x:
        print("YES")
    else:
        print("NO")
