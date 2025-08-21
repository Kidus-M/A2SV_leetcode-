import sys
from math import floor, log2
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * 30
    for x in a:
        high_bit = floor(log2(x))
        count[high_bit] += 1
    ans = 0
    for c in count:
        ans += (c * (c - 1)) // 2
    print(ans)