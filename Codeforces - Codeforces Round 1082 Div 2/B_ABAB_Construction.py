t = int(input())

INF = 10**18

for _ in range(t):
    n = int(input())
    s = input().strip()

    parity_n = n % 2
    dp_min = [INF, INF]
    dp_max = [-INF, -INF]

    dp_min[0] = dp_max[0] = 0

    for i in range(1, n + 1):
        ch = s[i - 1]

        next_min = [INF, INF]
        next_max = [-INF, -INF]

        for p in (0, 1):
            if dp_min[p] > dp_max[p]:
                continue

            left_char = 'a' if p == 0 else 'b'

            k = i - 1
            parity_k = k % 2
            right_parity = parity_n ^ (parity_k ^ p)
            right_char = 'a' if right_parity == 1 else 'b'

            can_left = (ch == '?' or ch == left_char)
            can_right = (ch == '?' or ch == right_char)

            if not can_left and not can_right:
                continue

            if can_left:
                new_p = p ^ 1
                next_min[new_p] = min(next_min[new_p], dp_min[p] + 1)
                next_max[new_p] = max(next_max[new_p], dp_max[p] + 1)

            if can_right:
                new_p = p
                next_min[new_p] = min(next_min[new_p], dp_min[p])
                next_max[new_p] = max(next_max[new_p], dp_max[p])

        dp_min, dp_max = next_min, next_max

    if dp_min[0] <= dp_max[0] or dp_min[1] <= dp_max[1]:
        print("YES")
    else:
        print("NO")