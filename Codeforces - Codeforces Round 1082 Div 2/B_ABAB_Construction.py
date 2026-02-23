t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())

    for i in range(n):
        if s[i] == '?':
            for c in ('a', 'b'):
                ok = True
                if i > 0 and s[i - 1] == c and (i - 1) % 2 == 1:
                    ok = False
                if i + 1 < n and s[i + 1] == c and i % 2 == 1:
                    ok = False
                if ok:
                    s[i] = c
                    break

    good = True
    for i in range(n - 1):
        if s[i] == s[i + 1] and i % 2 == 1:
            good = False
            break

    print("YES" if good else "NO")