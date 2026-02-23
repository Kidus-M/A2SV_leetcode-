t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    max_reach = [0] * n
    for i in range(n - 1, -1, -1):
        value = arr[i]
        end = i
        j = i + 1
        while j < n and arr[j] == value + 1:
            end = max_reach[j]
            j = end + 1
        max_reach[i] = end

    next_pos = [max_reach[i] + 1 for i in range(n)]

    adj = [[] for _ in range(n)]
    for i in range(n):
        if next_pos[i] < n:
            adj[next_pos[i]].append(i)

    num_l = [0] * n
    for i in range(n):
        num_l[i] = 1
        for pred in adj[i]:
            num_l[i] += num_l[pred]

    total = 0
    for i in range(n):
        total += num_l[i] * (n - i)

    print(total)