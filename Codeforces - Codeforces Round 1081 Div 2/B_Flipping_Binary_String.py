t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    ones = [str(i + 1) for i in range(n) if s[i] == '1']

    if len(ones) % 2 == 1:
        print(-1)
    else:
        print(len(ones))
        if ones:
            print(' '.join(sorted(ones)))
        else:
            print(end='') 