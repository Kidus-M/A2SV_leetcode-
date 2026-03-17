import sys
input = sys.stdin.readline

# number of product types
n = int(input())

products = []

for _ in range(n):
    a, b = map(int, input().split())
    products.append([a, b])

# sort products by the discount threshold b
# we try to unlock the smallest thresholds first
products.sort(key=lambda x: x[1])

# two pointers
l = 0          # product whose discount we want to unlock
r = n - 1      # product used as "filler" purchases when we need extra items

bought = 0     # total number of items purchased so far
cost = 0       # total money spent

while l <= r:

    # if we already bought enough items to unlock discount for product l
    if bought >= products[l][1]:

        # we can now buy all required items of product l at discounted price (1 ruble each)
        cost += products[l][0]

        # increase total items purchased
        bought += products[l][0]

        # move to the next product
        l += 1

    else:
        # we haven't unlocked the discount yet
        # we must buy more items first

        # how many more items are needed to unlock discount for product l
        need = products[l][1] - bought

        # take items from the product on the right side
        # these are products with large discount thresholds
        # so buying them early doesn't waste potential discounts
        take = min(need, products[r][0])

        # these purchases happen BEFORE discount
        # so each costs 2 rubles
        cost += take * 2

        # update total purchases
        bought += take

        # reduce remaining required items for product r
        products[r][0] -= take

        # if we finished all required items for product r
        if products[r][0] == 0:
            r -= 1   # move pointer left

# print minimum cost
print(cost)