import sys

input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    a=input().strip()
    b=input().strip()

    pa=[[0]*26 for _ in range(n+1)]
    pb = [[0] * 26 for _ in range(n + 1)]

    for i in range(1,n+1):
        for c in range(26):
            pa[i][c]=pa[i-1][c]
            pb[i][c] = pb[i - 1][c]
        pa[i][ord(a[i-1])-ord('a')] += 1
        pb[i][ord(b[i - 1]) - ord('a')] += 1


    for _ in range(q):
        l,r=map(int,input().split())
        same=0
        for c in range(26):
            fa=pa[r][c]-pa[l-1][c]
            fb = pb[r][c] - pb[l - 1][c]
            same += min(fa,fb)
        print((r-l+1)-same)