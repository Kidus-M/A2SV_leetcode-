import sys,threading
input = lambda: sys.stdin.readline().strip()



def main():
    n = int(input())
    a = list(map(int, input().split()))

    def getprimes(x):
        factors = set()
        while x % 2 == 0:
            factors.add(2)
            x //= 2
        f = 3
        while f * f <= x:
            while x % f == 0:
                factors.add(f)
                x //= f
            f += 2
        if x > 1:
            factors.add(x)
        return factors

    primes = [getprimes(num) for num in a]

    def shareCF(i, j):
        return not primes[i].isdisjoint(primes[j])

    memo = [-1] * n

    def dp(i):
        if memo[i] != -1:
            return memo[i]
        max_len = 1
        for j in range(i):
            if a[j] < a[i] and shareCF(i, j):
                max_len = max(max_len, dp(j) + 1)

        memo[i] = max_len
        return memo[i]

    ans = max(dp(i) for i in range(n))
    print(ans)


if __name__ == '__main__':
    sys.setrecursionlimit(200000)
    threading.stack_size(2 * 1024 * 1024)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
