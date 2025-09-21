import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

L = [1]*n
R = [1]*n
for i in range(1, n):
    if a[i] > a[i-1]:
        L[i] = L[i-1] + 1
for i in range(n-2, -1, -1):
    if a[i] < a[i+1]:
        R[i] = R[i+1] + 1

ans = max(L)
for i in range(1, n-1):
    if a[i-1] < a[i+1]:
        ans = max(ans, L[i-1] + R[i+1])
print(ans)
