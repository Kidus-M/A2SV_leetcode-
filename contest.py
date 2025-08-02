import sys, threading
from collections import Counter
input = lambda: sys.stdin.readline().strip()
def main():
    n=int(input())
    a=list(map(int, input().split()))
    count=Counter(a)

    memo={}
    def dp(x):
        if x==0:
            return 0
        if x==1:
            return count[1]
        if x in memo:
            return memo[x]
        memo[x]=max(dp(x-1), dp(x-2)+count[x]*x)
        return memo[x]
    print(dp(max(count)))


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
