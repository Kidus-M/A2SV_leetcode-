t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    a = []
    b = []

    i = 0
    while i < n:
        if s[i] == '1':
            a.append(i + 1)
        else:
            b.append(i + 1)
        i += 1

    if len(a) % 2 == 0:
        print(len(a))
        if len(a):
            print(*a)
        else:
            print()
    elif len(b) % 2 == 1:
        print(len(b))
        if len(b):
            print(*b)
        else:
            print()
    else:
        print(-1)