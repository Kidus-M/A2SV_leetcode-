import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, k, a1, ak = map(int, input().split())
    use_k = min(ak, m // k)
    m -= use_k * k
    use_1 = min(a1, m)
    m -= use_1
    fancy = (m + k - 1) // k
    print(fancy)