t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    distinct_values = len(set(a))
    print(2 * distinct_values - 1)
    