import sys

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out_lines = []
    for _ in range(t):
        n = int(data[idx]); m = int(data[idx+1]); l = int(data[idx+2])
        idx += 3
        a = [int(data[idx+i]) for i in range(n)]
        idx += n
        reset_times = set(a)

        dangers = [0] * m

        for sec in range(1, l + 1):
            # find the largest and the second largest danger
            max_val = -1
            second_val = -1
            max_idx = 0
            second_idx = 0
            for i in range(m):
                if dangers[i] > max_val:
                    second_val = max_val
                    second_idx = max_idx
                    max_val = dangers[i]
                    max_idx = i
                elif dangers[i] > second_val:
                    second_val = dangers[i]
                    second_idx = i

            # adversary increments the second largest
            dangers[second_idx] += 1

            # our turn: if this second is a reset time, reset the largest
            if sec in reset_times:
                # find the largest again (it may have changed)
                max_val = -1
                max_idx = 0
                for i in range(m):
                    if dangers[i] > max_val:
                        max_val = dangers[i]
                        max_idx = i
                dangers[max_idx] = 0

        answer = max(dangers)
        out_lines.append(str(answer))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()