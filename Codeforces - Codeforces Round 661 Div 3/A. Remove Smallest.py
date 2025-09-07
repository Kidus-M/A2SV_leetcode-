t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    can = True
    for i in range(1, n):
        if a[i] - a[i-1] > 1:
            can = False
            break
    print("YES" if can else "NO")