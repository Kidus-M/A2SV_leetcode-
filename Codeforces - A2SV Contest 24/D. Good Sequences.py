import sys,threading
from functools import lru_cache
input = lambda: sys.stdin.readline().strip()



def main():
    n = int(input())
    a = list(map(int, input().split()))

    def gcd(a,b):
        while b:
            a,b=b, a%b
        return a
    memo = [-1] * n
    @lru_cache(maxsize=None)
    def dp(i):
        if memo[i] != -1:
            return memo[i]
        max_len = 1
        for j in range(i):
            if a[j] < a[i] and gcd(a[i],a[j])>1:
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
