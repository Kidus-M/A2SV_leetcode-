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

    segments = 0
    i = 0
    while i < n:
        segments += 1
        i = max_reach[i] + 1

    print(segments)