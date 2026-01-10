t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    left = 1
    right = max(a) + x
    ans = 1

    while left <= right:
        mid = (left + right) // 2
        water = 0
        for v in a:
            if v < mid:
                water += mid - v
                if water > x:
                    break
        if water <= x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    print(ans)
