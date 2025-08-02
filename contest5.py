from collections import defaultdict
import sys, threading,math

input = lambda: sys.stdin.readline().strip()


def main():


    n=int(input())
    a=list(map(int, input().split()))
    count=defaultdict(int)
    maxx=0
    for num in a:
        count[num] += 1
        maxx=max(maxx,num)

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
    print(dp(maxx))



if __name__ == '__main__':
    sys.setrecursionlimit(200000)
    threading.stack_size(2 * 1024 * 1024)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
