import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
c1 = a.count(1)
c2 = a.count(2)
c3 = a.count(3)
dp = {}
for k in range(c3 + 1):
    for j in range(c2 + c3 + 1):
        for i in range(c1 + c2 + c3 + 1):
            if i + j + k == 0:
                dp[(i, j, k)] = 0.0
                continue
            total = i + j + k
            res = n / total
            if i > 0:
                res += (i / total) * dp.get((i - 1, j, k), 0.0)
            if j > 0:
                res += (j / total) * dp.get((i + 1, j - 1, k), 0.0)
            if k > 0:
                res += (k / total) * dp.get((i, j + 1, k - 1), 0.0)
            dp[(i, j, k)] = res
print(dp[(c1, c2, c3)])