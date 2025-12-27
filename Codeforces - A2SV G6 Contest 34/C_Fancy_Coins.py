import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, k, a1, ak = map(int, input().split())
    used_ak = min(m // k, ak)
    m -= used_ak * k
    if a1 >= m:
        print(0)
        continue
    remainder = m % k
    fancy_1_needed = max(0, remainder - a1)
    a1_left = max(0, a1 - remainder)
    k_chunks_needed = (m - remainder) // k
    fancy_k_needed = k_chunks_needed - (a1_left // k)
    print(fancy_1_needed + fancy_k_needed)