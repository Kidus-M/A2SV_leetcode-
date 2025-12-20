import sys
input = sys.stdin.readline

n, S = map(int, input().split())
a = list(map(int, input().split()))

low = 0
high = n
best_k = 0
best_cost = 0

while low <= high:
    mid = (low + high) // 2
    costs = []
    for i in range(n):
        costs.append(a[i] + (i + 1) * mid)
    costs.sort()
    total = sum(costs[:mid])
    if total <= S:
        best_k = mid
        best_cost = total
        low = mid + 1
    else:
        high = mid - 1

print(best_k, best_cost)