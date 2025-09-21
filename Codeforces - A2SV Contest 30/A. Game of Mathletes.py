import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    freq = Counter(arr)
    score = 0
    for x in list(freq.keys()):
        y = k - x
        if y not in freq:
            continue
        if x == y:
            score += freq[x] // 2
            freq[x] = 0
        else:
            m = min(freq[x], freq[y])
            score += m
            freq[x] -= m
            freq[y] -= m
    print(score)
