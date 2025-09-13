def gcd_range(a, b):
    if a == b:
        return a

    return 1


a, b = map(int, input().split())

print(gcd_range(a, b))