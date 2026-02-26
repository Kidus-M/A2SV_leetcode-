import sys

MOD = 998244353


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out_lines = []

    for _ in range(t):
        n = int(data[idx]);
        idx += 1
        T = [int(data[idx + j]) for j in range(n)];
        idx += n

        dp = [0] * (n + 1)
        dp[0] = 1
        prefix = [0] * (n + 1)
        prefix[0] = 1

        # last occurrence index for each value
        last = [-1] * 8005

        for i in range(1, n + 1):
            val = T[i - 1]

            # Base case: can always put a cut here
            dp[i] = prefix[i - 1]

            # If we've seen this value before, subtract the cases where it would create a duplicate
            if last[val] != -1:
                dp[i] = (dp[i] - prefix[last[val]]) % MOD

            prefix[i] = (prefix[i - 1] + dp[i]) % MOD
            last[val] = i - 1

        out_lines.append(str(dp[n] % MOD))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()