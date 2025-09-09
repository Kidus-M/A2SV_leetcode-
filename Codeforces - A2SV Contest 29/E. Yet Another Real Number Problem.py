
MOD = 10**9 + 7

def power(base, exponent):
    if exponent == 0:
        return 1
    half = power(base, exponent//2)
    if exponent % 2 == 0:
        return half *  half % MOD
    else:
        return base * half * half % MOD


def helper(x):
    two_division_count = 0
    while x & 1 == 0:
        x >>= 1
        two_division_count += 1
    return two_division_count

def solve():

    test = int(input())
    for _ in range(test):
        n = int(input())
        arr = list(map(int, input().split()))

        stack = []
        total_sum = 0
        ans = []

        for curr in arr:
            bit_pos = helper(curr)
            curr_res = curr >> bit_pos

            while stack:
                if bit_pos >= 30 or stack[-1][0] <= (curr_res << bit_pos):
                    bit_pos += stack[-1][1]
                    total_sum += stack[-1][0]
                    stack.pop()
                else:
                    break

            if bit_pos == 0:
                total_sum += curr_res
            else:
                stack.append((curr_res, bit_pos))

            res = total_sum
            for value, exponent in stack:
                res += power(2, exponent) * value % MOD
            ans.append(res)
        print(*ans)


solve()
