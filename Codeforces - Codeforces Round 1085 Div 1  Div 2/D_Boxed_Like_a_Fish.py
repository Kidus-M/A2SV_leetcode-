import sys

input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    m = int(data[index + 1])
    l = int(data[index + 2])
    index += 3

    a = [int(data[index + i]) for i in range(n)]
    index += n

    d = [0] * m
    flash_times = set(a)

    for sec in range(1, l + 1):
        min_val = min(d)
        j = d.index(min_val)
        d[j] += 1

        if sec in flash_times:
            max_val = max(d)
            k = d.index(max_val)
            d[k] = 0

    if max(d)==0:
        print("YES")
    else:
        print("NO")
