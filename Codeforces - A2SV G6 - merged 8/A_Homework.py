t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    m = int(input())
    b = input().strip()
    c = input().strip()

    result = list(a)

    for i in range(m):
        char = b[i]
        if c[i] == 'V':
            result.insert(0, char)
        else:
            result.append(char)

    print(''.join(result))