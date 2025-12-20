import sys

input = sys.stdin.readline

n, k = map(int, input().split())

if k % 2 == 0 or k > 2 * n - 1 or k < 1:
    print(-1)
else:
    a = list(range(1, n + 1))
    cur = 1
    def generate(l, r):
        global cur
        if cur >= k or r - l <= 1:
            return
        mid = (l + r) // 2
        a[mid - 1], a[mid] = a[mid], a[mid - 1]
        cur += 2
        generate(l, mid)
        generate(mid, r)


    generate(0, n)
    if cur == k:
        print(*a)
    else:
        print(-1)