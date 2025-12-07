import sys

sys.setrecursionlimit(2000)


def solve():

    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return
    if n >= 4:
        print("-1")
        return

    if n == 1:
        print("0")
        return
    grid_rows = []
    for _ in range(n):
        grid_rows.append(next(iterator))
    cols = []
    for j in range(m):
        val = 0
        for i in range(n):
            if grid_rows[i][j] == '1':
                val |= (1 << i)
        cols.append(val)
    cost_table = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            cost_table[i][j] = bin(i ^ j).count('1')

    if n == 2:
        cost_even = []
        cost_odd = []

        for c in cols:
            cost_even.append(min(cost_table[c][0], cost_table[c][3]))
            cost_odd.append(min(cost_table[c][1], cost_table[c][2]))

        ans1 = sum(cost_even[j] if j % 2 == 0 else cost_odd[j] for j in range(m))
        ans2 = sum(cost_odd[j] if j % 2 == 0 else cost_even[j] for j in range(m))

        print(min(ans1, ans2))
        return
    if n == 3:
        adj = [[] for _ in range(8)]
        for curr in range(8):
            for prev in range(8):
                p0, p1 = (prev & 1), (prev >> 1) & 1
                c0, c1 = (curr & 1), (curr >> 1) & 1
                if (p0 + p1 + c0 + c1) % 2 == 0: continue

                p2 = (prev >> 2) & 1
                c2 = (curr >> 2) & 1
                if (p1 + p2 + c1 + c2) % 2 == 0: continue

                adj[curr].append(prev)

        current_col_val = cols[0]
        dp = [cost_table[current_col_val][mask] for mask in range(8)]

        for j in range(1, m):
            new_dp = [float('inf')] * 8
            col_val = cols[j]

            for mask in range(8):
                base_cost = cost_table[col_val][mask]

                min_prev = float('inf')
                for prev in adj[mask]:
                    if dp[prev] < min_prev:
                        min_prev = dp[prev]

                if min_prev != float('inf'):
                    new_dp[mask] = min_prev + base_cost

            dp = new_dp

        print(min(dp))
solve()