from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)
    mx = max(freq.values())

    print(max(0, 2 * mx - n))
