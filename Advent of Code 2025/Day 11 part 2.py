import sys


def count_paths(node, target, graph, memo):
    if node == target:
        return 1
    if node in memo:
        return memo[node]

    # If a node has no outgoing connections (dead end) and isn't target
    if node not in graph:
        return 0

    total_paths = 0
    for neighbor in graph[node]:
        total_paths += count_paths(neighbor, target, graph, memo)

    memo[node] = total_paths
    return total_paths


def main():
    try:
        with open('input.txt', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return

    graph = {}

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Parse line: "bbb: ddd eee"
        if ':' in line:
            src, dests_str = line.split(':', 1)
            src = src.strip()
            dests = [d.strip() for d in dests_str.split()]
            graph[src] = dests

    # Helper to calculate paths between two nodes with a fresh memo
    def get_count(start, end):
        return count_paths(start, end, graph, {})

    # We need paths from 'svr' to 'out' visiting BOTH 'dac' and 'fft'.
    # Since flow is one-way (DAG), the order is either:
    # 1. svr -> ... -> dac -> ... -> fft -> ... -> out
    # 2. svr -> ... -> fft -> ... -> dac -> ... -> out

    # Path set 1: svr -> dac -> fft -> out
    p1 = get_count('svr', 'dac') * get_count('dac', 'fft') * get_count('fft', 'out')
    p2 = get_count('svr', 'fft') * get_count('fft', 'dac') * get_count('dac', 'out')

    print(p1 + p2)


if __name__ == '__main__':
    sys.setrecursionlimit(20000)
    main()