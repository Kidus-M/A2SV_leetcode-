t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    gold = 0
    given = 0

    for x in a:
        if x >= k:
            gold += x
        elif x == 0 and gold > 0:
            gold -= 1
            given += 1

    print(given)
