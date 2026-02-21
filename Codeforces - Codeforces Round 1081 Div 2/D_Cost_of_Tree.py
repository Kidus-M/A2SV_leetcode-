buf = []
while True:
    try:
        s = input()
        for x in s.split():
            buf.append(x)
    except:
        break

if not buf:
    exit()

ptr = 0
t = int(buf[ptr])
ptr += 1

for _ in range(t):
    n = int(buf[ptr])
    ptr += 1
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(buf[ptr])
        ptr += 1

    g = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        u = int(buf[ptr])
        v = int(buf[ptr + 1])
        ptr += 2
        g[u].append(v)
        g[v].append(u)

    o = []
    p = [0] * (n + 1)
    d = [0] * (n + 1)
    q = [1]
    qh = 0
    while qh < len(q):
        u = q[qh]
        qh += 1
        o.append(u)
        for v in g[u]:
            if v != p[u]:
                p[v] = u
                d[v] = d[u] + 1
                q.append(v)

    s = [0] * (n + 1)
    c = [0] * (n + 1)
    md = [0] * (n + 1)
    hv = [0] * (n + 1)
    md2 = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        u = o[i]
        s[u] = a[u]
        md[u] = d[u]
        bc = 0
        bd = d[u]
        for v in g[u]:
            if v != p[u]:
                s[u] += s[v]
                c[u] += c[v] + s[v]
                if md[v] > bd:
                    bd = md[v]
                    bc = v
        md[u] = bd
        hv[u] = bc

        bd2 = d[u]
        for v in g[u]:
            if v != p[u] and v != bc:
                if md[v] > bd2:
                    bd2 = md[v]
        md2[u] = bd2

    vis = [False] * (n + 1)
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        if vis[i]:
            continue
        ph = []
        cu = i
        while cu != 0:
            vis[cu] = True
            ph.append(cu)
            cu = hv[cu]

        k = len(ph)
        vl = [0] * k
        for j in range(k):
            vl[j] = md2[ph[j]]

        ml = [0] * k
        for j in range(k):
            u = ph[j]
            lq = []
            for v in g[u]:
                if v != p[u] and v != hv[u]:
                    lq.append(v)
            bl = 0
            lh = 0
            while lh < len(lq):
                cl = lq[lh]
                lh += 1
                pr = s[cl] * (md[ph[-1]] - d[cl] + 1)
                if pr > bl:
                    bl = pr
                for v in g[cl]:
                    if v != p[cl]:
                        lq.append(v)
            ml[j] = bl

        ao = [0] * k
        cm = 0
        for j in range(k - 1, -1, -1):
            if ml[j] > cm:
                cm = ml[j]
            ao[j] = cm

        R = [k] * k
        st = []
        for j in range(k - 1, -1, -1):
            while len(st) > 0 and vl[st[-1]] <= vl[j]:
                st.pop()
            if len(st) > 0:
                R[j] = st[-1]
            st.append(j)

        tr = [[] for _ in range(2 * k)]
        for j in range(k):
            tr[k + j].append((s[ph[j]], s[ph[j]] * (1 - d[ph[j]])))

        for j in range(k - 1, 0, -1):
            A_arr = tr[2 * j]
            B_arr = tr[2 * j + 1]
            mg = []
            ai = 0
            bi = 0
            while ai < len(A_arr) and bi < len(B_arr):
                if A_arr[ai][0] < B_arr[bi][0] or (A_arr[ai][0] == B_arr[bi][0] and A_arr[ai][1] > B_arr[bi][1]):
                    mg.append(A_arr[ai])
                    ai += 1
                else:
                    mg.append(B_arr[bi])
                    bi += 1
            while ai < len(A_arr):
                mg.append(A_arr[ai])
                ai += 1
            while bi < len(B_arr):
                mg.append(B_arr[bi])
                bi += 1

            hl = []
            for mm, cc in mg:
                if len(hl) > 0 and hl[-1][0] == mm:
                    continue
                while len(hl) >= 2:
                    m1, c1 = hl[-2]
                    m2, c2 = hl[-1]
                    if (c1 - c2) * (mm - m2) >= (c2 - cc) * (m2 - m1):
                        hl.pop()
                    else:
                        break
                hl.append((mm, cc))
            tr[j] = hl

        A = [0] * k
        for j in range(k - 1, -1, -1):
            ql = j + 1
            qr = R[j] if R[j] < k else k - 1
            qa = 0
            if ql <= qr:
                L = ql + k
                R_seg = qr + k
                xx = vl[j]
                while L <= R_seg:
                    if L % 2 == 1:
                        h = tr[L]
                        if len(h) > 0:
                            ll = 0
                            rr = len(h) - 1
                            while ll < rr:
                                mid = (ll + rr) // 2
                                y1 = h[mid][0] * xx + h[mid][1]
                                y2 = h[mid + 1][0] * xx + h[mid + 1][1]
                                if y1 <= y2:
                                    ll = mid + 1
                                else:
                                    rr = mid
                            vv = h[ll][0] * xx + h[ll][1]
                            if vv > qa:
                                qa = vv
                        L += 1
                    if R_seg % 2 == 0:
                        h = tr[R_seg]
                        if len(h) > 0:
                            ll = 0
                            rr = len(h) - 1
                            while ll < rr:
                                mid = (ll + rr) // 2
                                y1 = h[mid][0] * xx + h[mid][1]
                                y2 = h[mid + 1][0] * xx + h[mid + 1][1]
                                if y1 <= y2:
                                    ll = mid + 1
                                else:
                                    rr = mid
                            vv = h[ll][0] * xx + h[ll][1]
                            if vv > qa:
                                qa = vv
                        R_seg -= 1
                    L //= 2
                    R_seg //= 2

            na = A[R[j]] if R[j] < k else 0
            if qa > na:
                A[j] = qa
            else:
                A[j] = na

        for j in range(k):
            u = ph[j]
            mx = ao[j]
            if A[j] > mx:
                mx = A[j]
            ans[u] = c[u] + mx

    out = []
    for i in range(1, n + 1):
        out.append(str(ans[i]))
    print(" ".join(out))