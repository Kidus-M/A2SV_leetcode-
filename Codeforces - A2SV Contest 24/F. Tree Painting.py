import sys, threading

input = lambda: sys.stdin.readline().strip()


def main():
    n=int(input())
    adj=[[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)

    subtree=[1] *(n+1)
    def subsize(v,parent):
        for u in adj[v]:
            if u != parent:
                subsize(u,v)
                subtree[v]+=subtree[u]

    subsize(1,0)

    memo={}
    def dp(v,parent,ispainted):
        if (v, parent,ispainted) in memo:
            return memo[(v, parent,ispainted)]
        if ispainted:
            return 0
        wc=0
        for u in adj[v]:
            if u !=parent:
                wc += dp(u,v,0)

        cs=subtree[v]- (1 if ispainted else 0)
        for u in adj[v]:
            if u != parent:
                cs += dp(u,v,1)
        points=max(0,cs-1)

        result=max(points, dp(v,parent,1))
        memo[(v, parent, ispainted)]=result
        return result
    ans=dp(1,0,0)
    print(ans)




if __name__ == '__main__':
    sys.setrecursionlimit(200000)
    threading.stack_size(2 * 1024 * 1024)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
