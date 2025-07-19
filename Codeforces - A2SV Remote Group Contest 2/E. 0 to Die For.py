import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    zero_pos = []
    for idx, c in enumerate(s):
        if c == '0':
            zero_pos.append(idx)

    m = len(zero_pos)
    res = [-1] * n
    if m == 0:
        print(' '.join(map(str, res)))
        continue

    prefix = [0] * (m + 1)
    for i in range(m):
        prefix[i + 1] = prefix[i] + zero_pos[i]

    for i in range(1, n + 1):
        if i > m:
            res[i - 1] = -1
            continue
        k = i
        sum_target = k * (2 * n - k - 1) // 2
        l = m - k
        r = m - 1
        sum_original = prefix[r + 1] - prefix[l]
        res[i - 1] = sum_target - sum_original

    print(' '.join(map(str, res)))