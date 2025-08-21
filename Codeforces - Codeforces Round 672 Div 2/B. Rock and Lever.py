import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * 30
    for x in a:
        high_bit = 0
        while x > 0:
            x >>= 1
            high_bit += 1
        count[high_bit - 1] += 1
    ans = 0
    for c in count:
        ans += (c * (c - 1)) // 2
    print(ans)