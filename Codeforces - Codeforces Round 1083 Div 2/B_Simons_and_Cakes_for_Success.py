t = int(input())

for _ in range(t):
    n = int(input())

    remaining = n
    result = 1

    if remaining % 2 == 0:
        result *= 2
        while remaining % 2 == 0:
            remaining //= 2

    factor = 3
    while factor * factor <= remaining:
        if remaining % factor == 0:
            result *= factor
            while remaining % factor == 0:
                remaining //= factor
        factor += 2

    if remaining > 1:
        result *= remaining

    print(result)