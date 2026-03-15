import sys

input = sys.stdin.readline

n = int(input())
products = []

for _ in range(n):
    a, b = map(int, input().split())
    products.append([a, b])

products.sort(key=lambda x: x[1])

l = 0
r = n - 1
bought = 0
cost = 0

while l <= r:
    if bought >= products[l][1]:
        cost += products[l][0]
        bought += products[l][0]
        l += 1
    else:
        need = products[l][1] - bought
        take = min(need, products[r][0])

        cost += take * 2
        bought += take
        products[r][0] -= take

        if products[r][0] == 0:
            r -= 1

print(cost)