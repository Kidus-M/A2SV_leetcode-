t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    c1 = s.count('1')
    c0 = n - c1

    if c1 % 2 == 0:
        ans = []
        i = 0
        while i < n:
            if s[i] == '1':
                ans.append(str(i + 1))
            i += 1
        print(len(ans))
        if ans:
            print(" ".join(ans))
    elif c0 % 2 == 1:
        ans = []
        i = 0
        while i < n:
            if s[i] == '0':
                ans.append(str(i + 1))
            i += 1
        print(len(ans))
        print(" ".join(ans))
    else:
        print(-1)