class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        a = b = c = d = 0
        while t % 2 == 0:
            t //= 2; a += 1
        while t % 3 == 0:
            t //= 3; b += 1
        while t % 5 == 0:
            t //= 5; c += 1
        while t % 7 == 0:
            t //= 7; d += 1
        if t != 1:
            return "-1"

        e2 = {1:0,2:1,3:0,4:2,5:0,6:1,7:0,8:3,9:0}
        e3 = {1:0,2:0,3:1,4:0,5:0,6:1,7:0,8:0,9:2}

        MAXA, MAXB = 60, 40
        contrib = [(1,0),(0,1),(2,0),(1,1),(3,0),(0,2)]
        dp = [[0]*(MAXB+1) for _ in range(MAXA+1)]
        INF = float('inf')
        for i in range(MAXA+1):
            for j in range(MAXB+1):
                if i == 0 and j == 0:
                    continue
                best = INF
                for da, db in contrib:
                    pi = i - da if i - da > 0 else 0
                    pj = j - db if j - db > 0 else 0
                    if pi == i and pj == j:
                        continue
                    v = dp[pi][pj] + 1
                    if v < best:
                        best = v
                dp[i][j] = best

        def cover_cost(ra, rb):
            if ra < 0: ra = 0
            if rb < 0: rb = 0
            if ra > MAXA: ra = MAXA
            if rb > MAXB: rb = MAXB
            return dp[ra][rb]

        def feasible(ra, rb, rc, rd, m):
            ra = max(ra, 0); rb = max(rb, 0); rc = max(rc, 0); rd = max(rd, 0)
            if rc + rd > m:
                return False
            rem = m - rc - rd
            return cover_cost(ra, rb) <= rem

        def build(ra, rb, rc, rd, m):
            res = []
            for pos in range(m):
                rem_after = m - pos - 1
                for dgt in range(1, 10):
                    nra = ra - e2[dgt]
                    nrb = rb - e3[dgt]
                    nrc = rc - (1 if dgt == 5 else 0)
                    nrd = rd - (1 if dgt == 7 else 0)
                    if feasible(nra, nrb, nrc, nrd, rem_after):
                        res.append(str(dgt))
                        ra, rb, rc, rd = max(nra,0), max(nrb,0), max(nrc,0), max(nrd,0)
                        break
            return ''.join(res)

        n = len(num)
        digits = [int(ch) for ch in num]

        pa = [0]*(n+1); pb = [0]*(n+1); pc = [0]*(n+1); pd = [0]*(n+1)
        prefix_zero_free = [True]*(n+1)
        for i in range(n):
            dg = digits[i]
            pa[i+1] = pa[i] + e2.get(dg, 0)
            pb[i+1] = pb[i] + e3.get(dg, 0)
            pc[i+1] = pc[i] + (1 if dg == 5 else 0)
            pd[i+1] = pd[i] + (1 if dg == 7 else 0)
            prefix_zero_free[i+1] = prefix_zero_free[i] and dg != 0

        if prefix_zero_free[n] and pa[n] >= a and pb[n] >= b and pc[n] >= c and pd[n] >= d:
            return num

        answer = None
        for i in range(n - 1, -1, -1):
            if not prefix_zero_free[i]:
                continue
            ra0 = a - pa[i]; rb0 = b - pb[i]; rc0 = c - pc[i]; rd0 = d - pd[i]
            m = n - i - 1
            found_d = None
            for dgt in range(digits[i] + 1, 10):
                nra = ra0 - e2[dgt]; nrb = rb0 - e3[dgt]
                nrc = rc0 - (1 if dgt == 5 else 0)
                nrd = rd0 - (1 if dgt == 7 else 0)
                if feasible(nra, nrb, nrc, nrd, m):
                    found_d = dgt
                    break
            if found_d is not None:
                nra = max(ra0 - e2[found_d], 0); nrb = max(rb0 - e3[found_d], 0)
                nrc = max(rc0 - (1 if found_d == 5 else 0), 0)
                nrd = max(rd0 - (1 if found_d == 7 else 0), 0)
                answer = num[:i] + str(found_d) + build(nra, nrb, nrc, nrd, m)
                break

        if answer is not None:
            return answer

        L = n + 1
        minlen = c + d + cover_cost(a, b)
        if minlen > L:
            L = minlen
        return build(a, b, c, d, L)