import sys

def construct(l, r, remaining_k, perm):
    if r - l <= 0:
        return
    if r - l == 1:
        perm[l] = current[0]
        current[0] += 1
        return
    mid = l + (r - l) // 2
    if remaining_k > 0:
        construct(mid, r, remaining_k - 1, perm)
        construct(l, mid, 0, perm)
        perm[mid - 1], perm[mid] = perm[mid], perm[mid - 1]
    else:
        construct(l, mid, 0, perm)
        construct(mid, r, 0, perm)

input = sys.stdin.readline
n, k = map(int, input().split())

if k % 2 == 0 or k > 2 * n - 1:
    print(-1)
else:
    perm = [0] * n
    current = [1]
    construct(0, n, k - 1, perm)
    print(' '.join(map(str, perm)))