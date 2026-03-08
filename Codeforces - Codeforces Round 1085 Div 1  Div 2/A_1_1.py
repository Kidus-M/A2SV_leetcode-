t = int(input())
for _ in range(t):
    m = int(input())
    a = input().strip()

    x = 0
    y = 0
    p = 0

    while p < m:
        if a[p] != '1':
            p += 1
            continue

        st = p
        c = 0
        g = 0

        while True:
            while p < m and a[p] == '1':
                c += 1
                p += 1

            if p + 1 >= m or a[p] != '0' or a[p+1] != '1':
                break

            g += 1
            p += 1

        ed = p - 1
        ln = ed - st + 1

        if ln > 0:
            y += ln - (ln - 1) // 2

        x += c + g

    print(y, x)