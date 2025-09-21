import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = sorted(map(int, input().split()))
    l, r = 0, n - 1
    score = 0
    while l < r:
        s = arr[l] + arr[r]
        if s == k:
            score += 1
            l += 1
            r -= 1
        elif s < k:
            l += 1
        else:
            r -= 1
    print(score)
