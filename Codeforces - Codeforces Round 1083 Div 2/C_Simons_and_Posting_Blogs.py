t = int(input())

for _ in range(t):
    bc = int(input())

    blogs = []
    allu = set()

    for _ in range(bc):
        arr = list(map(int, input().split()))
        b = arr[1:]
        blogs.append(b)
        for x in b:
            allu.add(x)

    rem = set(allu)
    res = []

    while rem:
        smalltail = 10**18

        for b in blogs:
            for i in range(len(b) - 1, -1, -1):
                if b[i] in rem:
                    smalltail = min(smalltail, b[i])
                    break

        best = None

        for b in blogs:
            tail = 10**18
            for i in range(len(b) - 1, -1, -1):
                if b[i] in rem:
                    tail = b[i]
                    break

            if tail == smalltail:
                cur = []
                used = set()
                for i in range(len(b) - 1, -1, -1):
                    v = b[i]
                    if v in rem and v not in used:
                        cur.append(v)
                        used.add(v)

                if best is None or cur < best:
                    best = cur

        for v in best:
            res.append(v)
            rem.remove(v)

    print(' '.join(map(str, res)))