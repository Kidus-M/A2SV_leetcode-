import sys


def solve():
    # Read number of test cases
    line = sys.stdin.readline()
    if not line:
        return
    try:
        t_cases = int(line.strip())
    except ValueError:
        return

    for _ in range(t_cases):
        # Read n, handling potential empty lines between cases
        line = sys.stdin.readline()
        while line and not line.strip():
            line = sys.stdin.readline()
        if not line:
            break
        n = int(line.strip())

        # Step 1: Compute DP values (longest path from each node)
        # We query the longest path starting at 'i' using ALL nodes.
        dist = {}
        all_nodes = [str(x) for x in range(1, n + 1)]
        full_set_str = " ".join(all_nodes)

        for i in range(1, n + 1):
            # Query format: ? x k s1 ... sk
            print(f"? {i} {n} {full_set_str}")
            sys.stdout.flush()

            try:
                response = sys.stdin.readline()
                if not response:
                    break
                val = int(response.strip())
            except ValueError:
                sys.exit(0)  # Should not happen with correct interactor

            if val == -1:
                sys.exit(0)

            dist[i] = val

        # Group nodes by their max path length (layers)
        layers = {}
        max_len = 0
        start_node = -1

        for i in range(1, n + 1):
            d = dist[i]
            if d > max_len:
                max_len = d
                start_node = i
            if d not in layers:
                layers[d] = []
            layers[d].append(i)

        # Step 2: Reconstruct the path
        path = [start_node]
        curr = start_node

        # Iterate downwards from the layer below the start node
        for d in range(max_len - 1, 0, -1):
            candidates = layers[d]

            if len(candidates) == 1:
                nxt = candidates[0]
            else:
                # Binary search to find a neighbor in this layer
                low = 0
                high = len(candidates) - 1

                # We know 'curr' connects to at least one node in 'candidates'
                while low < high:
                    mid = (low + high) // 2
                    # Try the left half: candidates[low ... mid]
                    left_subset = candidates[low: mid + 1]

                    # Query: curr + left_subset
                    # Since layers[d] is an independent set, the longest path
                    # in {curr} U left_subset is 2 if connected, 1 otherwise.
                    query_list = left_subset + [curr]
                    query_str = " ".join(str(x) for x in query_list)

                    print(f"? {curr} {len(query_list)} {query_str}")
                    sys.stdout.flush()

                    try:
                        ans = int(sys.stdin.readline().strip())
                    except ValueError:
                        sys.exit(0)

                    if ans == -1:
                        sys.exit(0)

                    if ans == 2:
                        # Connection found in left half
                        high = mid
                    else:
                        # Connection must be in right half
                        low = mid + 1

                nxt = candidates[low]

            path.append(nxt)
            curr = nxt

        # Output the result
        # Format: ! k v1 ... vk
        path_str = " ".join(str(x) for x in path)
        print(f"! {len(path)} {path_str}")
        sys.stdout.flush()


if __name__ == "__main__":
    solve()