t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    d = x - 2 * y
    if d < 0 or d % 3 != 0:
        print("NO")
        continue

    t2 = d // 3
    lo = 0
    if y < 0:
        lo = -y
    hi = t2 // 2

    if lo <= hi:
        print("YES")
    else:
        print("NO")