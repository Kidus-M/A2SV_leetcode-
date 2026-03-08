import sys


def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    t = int(data[0])
    out = []
    idx = 1

    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        l = int(data[idx + 2])
        idx += 3

        a = []
        for _ in range(n):
            a.append(int(data[idx]))
            idx += 1

        # Binary search for the minimum possible x
        low = 0
        high = l
        ans = l

        while low <= high:
            mid = (low + high) // 2

            # Check if x = mid is winnable for the night guard
            # C[k] will store the maximum allowed sum of the top k animatronics
            # going backwards from time l to 0
            C = [k * mid for k in range(m + 1)]

            last_time = l
            possible = True

            for i in range(n - 1, -1, -1):
                flash_time = a[i]
                delta = last_time - flash_time

                # Time passes backwards: the opponent must have added `delta` to the total sum
                for k in range(1, m + 1):
                    C[k] -= delta

                # Check if capacities dropped below 0
                if C[m] < 0:
                    possible = False
                    break

                # A flash happened at `flash_time`:
                # The top element was eliminated, meaning the remaining m-1 elements
                # were bound by the previous capacities.
                new_C = [0] * (m + 1)
                for k in range(1, m):
                    new_C[k] = C[k + 1]
                new_C[m] = C[m]

                # Make sure the capacity bounds stay monotonic and non-negative logically
                for k in range(1, m + 1):
                    if k < m and new_C[k] > new_C[k + 1]:
                        new_C[k] = new_C[k + 1]

                C = new_C
                last_time = flash_time

            # Remaining time down to 0
            delta = last_time - 0
            for k in range(1, m + 1):
                C[k] -= delta

            # At time 0, all animatronics start at 0 danger level.
            # So the capacity for the sum of the top k must be >= 0.
            if C[m] < 0:
                possible = False

            for k in range(1, m + 1):
                if C[k] < 0:
                    possible = False
                    break

            if possible:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        out.append(str(ans))

    print('\n'.join(out))


if __name__ == '__main__':
    solve()