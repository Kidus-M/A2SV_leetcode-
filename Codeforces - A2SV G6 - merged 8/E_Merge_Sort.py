import sys


def construct(l, r, perm, val):
    if l >= r:
        return
    if l + 1 == r:
        perm[l] = val[0]
        val[0] += 1
        return

    mid = (l + r) // 2

    construct(l, mid, perm, val)
    construct(mid, r, perm, val)

    if remaining[0] > 0:
        remaining[0] -= 1
        perm[mid - 1], perm[mid] = perm[mid], perm[mid - 1]


input = sys.stdin.readline
n, k = map(int, input().split())

if k % 2 == 0 or k > 2 * n - 1:
    print(-1)
    sys.exit()

perm = [0] * n
val = [1]
remaining = [k - 1]

construct(0, n, perm, val)

print(' '.join(map(str, perm)))