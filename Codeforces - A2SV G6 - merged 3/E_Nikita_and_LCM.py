import sys, math
input = sys.stdin.readline

def lcm(a, b):
    return a // math.gcd(a, b) * b


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr_set = set(arr)

    # Step 1: Compute LCM of whole array
    L = 1
    for x in arr:
        L = lcm(L, x)

    # If L is NOT in the array, answer is n immediately
    if L not in arr_set:
        print(n)
        continue

    # Step 2: Factorize L
    tmp = L
    prime_pows = []
    d = 2
    while d * d <= tmp:
        if tmp % d == 0:
            cnt = 0
            while tmp % d == 0:
                tmp //= d
                cnt += 1
            prime_pows.append((d, cnt))
        d += 1 if d == 2 else 2
    if tmp > 1:
        prime_pows.append((tmp, 1))

    # Step 3: Generate all divisors of L
    divisors = [1]
    for p, e in prime_pows:
        new_list = []
        mul = 1
        for _ in range(e + 1):
            for v in divisors:
                new_list.append(v * mul)
            mul *= p
        divisors = new_list

    # Step 4: Precompute mapping divisor → elements that divide it
    # Prepare dictionary: d -> list of elements
    div_map = {d: [] for d in divisors}

    for x in arr:
        for d in divisors:
            if d % x == 0:
                div_map[d].append(x)

    # Step 5: For each divisor, compute LCM of mapped elements
    answer = 0

    for d in divisors:
        if d in arr_set:
            continue  # LCM equal to element in arr → invalid

        elems = div_map[d]
        if not elems:
            continue

        cur_lcm = 1
        for x in elems:
            cur_lcm = lcm(cur_lcm, x)
            if cur_lcm > d:  # early cut
                break

        # Check if subsequence LCM is EXACTLY d
        if cur_lcm == d:
            answer = max(answer, len(elems))

    print(answer)
