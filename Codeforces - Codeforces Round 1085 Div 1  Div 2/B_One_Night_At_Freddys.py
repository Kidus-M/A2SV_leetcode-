import sys


def solve():
    # Read all input at once and split by whitespace
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    t = int(input_data[ptr])
    ptr += 1

    results = []

    for _ in range(t):
        n = int(input_data[ptr])
        k = int(input_data[ptr + 1])
        m = int(input_data[ptr + 2])
        ptr += 3

        # Read the array 'a'
        a = []
        for i in range(n):
            a.append(int(input_data[ptr]))
            ptr += 1

        a.sort()

        ans = 0

        # 1. Handle the gap from the beginning (1 to a[0])
        if a[0] > 1:
            ans += (a[0] - 1) // k

        # 2. Handle the gaps between elements in the array
        for i in range(1, n):
            gap = a[i] - a[i - 1] - 1
            if gap > 0:
                ans += gap // k

        # 3. Handle the gap from the last element to m
        if m > a[n - 1]:
            ans += (m - a[n - 1]) // k

        results.append(str(ans))

    # Print all results at once for speed
    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()