import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, H = map(int, input().split())
    a = list(map(int, input().split()))

    L = [0]*n
    for i in range(n):
        s = 0
        mx = 0
        k = i
        while k >= 0:
            if a[k] > mx:
                mx = a[k]
            s += H - mx
            k -= 1

        mx = a[i]
        cur = s
        j = i
        while j < n:
            if a[j] > mx:
                mx = a[j]
            if j > i:
                cur += H - mx
            if cur > L[j]:
                L[j] = cur
            j += 1

    R = [0]*n
    for i in range(n):
        s = 0
        mx = 0
        k = i
        while k < n:
            if a[k] > mx:
                mx = a[k]
            s += H - mx
            k += 1

        mx = a[i]
        cur = s
        j = i
        while j >= 0:
            if a[j] > mx:
                mx = a[j]
            if j < i:
                cur += H - mx
            if cur > R[j]:
                R[j] = cur
            j -= 1

    ans = 0
    for i in range(n):
        v = L[i] + R[i] - (H - a[i])
        if v > ans:
            ans = v

    print(ans)