t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))

    low = 1
    high = h  
    ans = h

    while low <= high:
        mid = (low + high) // 2
        total = 0
        for i in range(n):
            if i == n - 1:
                total += mid
            else:
                total += min(mid, a[i + 1] - a[i])
        if total >= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    print(ans)