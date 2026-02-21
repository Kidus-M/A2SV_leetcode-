t = int(input())
for _ in range(t):
    y = int(input())
    z = input()

    c = 0
    for i in range(y):
        if z[i] != z[(i + 1) % y]:
            c += 1

    if c + 1 < y:
        print(c + 1)
    else:
        print(y)