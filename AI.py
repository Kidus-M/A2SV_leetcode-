import heapq

# -----------------------------
# GRAPH INPUT FUNCTIONS
# -----------------------------
def get_graph_from_user():
    print("\n=== GRAPH INPUT ===")
    n = int(input("Enter number of nodes: "))

    print("Enter node names (one per line):")
    nodes = [input().strip() for _ in range(n)]

    graph = {node: {} for node in nodes}

    print("\nEnter number of edges:")
    e = int(input())

    print("\nEnter edges in format: node1 node2 cost")
    print("Example: Kazanchis Aratkilo 125\n")

    for _ in range(e):
        a, b, w = input().split()
        w = float(w)
        graph[a][b] = w
        graph[b][a] = w     # undirected graph

    return graph, nodes

def get_heuristics_from_user(nodes):
    print("\n=== HEURISTIC INPUT (for A*) ===")
    print("Enter heuristic values in format: node value")
    print("Enter 0 for the goal node.\n")

    heuristic = {}

    for node in nodes:
        h = float(input(f"h({node}) = "))
        heuristic[node] = h

    return heuristic


# -----------------------------
# UNIFORM COST SEARCH (UCS)
# -----------------------------
def uniform_cost_search(graph, start, goal):
    pq = [(0, start, [])]  # (cost, node, path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        path = path + [node]

        if node == goal:
            return path, cost

        for neigh, w in graph[node].items():
            if neigh not in visited:
                heapq.heappush(pq, (cost + w, neigh, path))

    return None, float("inf")


# -----------------------------
# A* SEARCH
# -----------------------------
def a_star(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start, [])]  # (f, g, node, path)
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        path = path + [node]

        if node == goal:
            return path, g

        for neigh, w in graph[node].items():
            if neigh not in visited:
                g2 = g + w
                f2 = g2 + heuristic[neigh]
                heapq.heappush(pq, (f2, g2, neigh, path))

    return None, float("inf")


# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main():
    print("\n===============================")
    print("   ROUTE FINDER (UCS / A*)")
    print("===============================")

    graph, nodes = get_graph_from_user()

    print("\nAvailable nodes:", nodes)
    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    print("\nChoose Algorithm:")
    print("1. Uniform Cost Search (UCS)")
    print("2. A* Search")
    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        path, cost = uniform_cost_search(graph, start, goal)
        print("\n=== UCS RESULT ===")
        print("Path:", " -> ".join(path))
        print("Total Cost:", cost)

    elif choice == "2":
        heuristic = get_heuristics_from_user(nodes)
        path, cost = a_star(graph, heuristic, start, goal)
        print("\n=== A* RESULT ===")
        print("Path:", " -> ".join(path))
        print("Total Cost:", cost)

    else:
        print("Invalid choice!")

# Run program
main()
