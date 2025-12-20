import sys


def build(l, r, swaps_left, perm, val):
    if l >= r:
        return swaps_left
    if l + 1 == r:
        perm[l] = val[0]
        val[0] += 1
        return swaps_left

    mid = (l + r) // 2

    swaps_left = build(l, mid, swaps_left, perm, val)
    swaps_left = build(mid, r, swaps_left, perm, val)

    if swaps_left > 0:
        perm[mid - 1], perm[mid] = perm[mid], perm[mid - 1]
        swaps_left -= 1

    return swaps_left


input = sys.stdin.readline
n, k = map(int, input().split())

if k % 2 == 0 or k > 2 * n - 1 or k < 1:
    print(-1)
else:
    perm = [0] * n
    val = [1]
    remaining_swaps = k - 1
    final_swaps = build(0, n, remaining_swaps, perm, val)
    if final_swaps != 0:
        print(-1)
    else:
        print(' '.join(map(str, perm)))