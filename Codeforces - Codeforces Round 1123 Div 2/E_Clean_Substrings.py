import sys
input=sys.stdin.readline
t=int(input())
out=[]

for _ in range(t):
    n,q=map(int,input().split())
    s=[int(ch) for ch in input().strip()]

    def edge(j):
        if 0<=j<n-1 and s[j]!=s[j+1]:
            return (j+1)*(n-j-1)
        return 0

    tot=0
    for j in range(n-1):
        tot += edge(j)

    c1=sum(s)

    res=[(tot+c1*(n-c1))//2]
    for _ in range(q):
        i=int(input())-1
        tot -= edge(i-1)+edge(i)
        c1 += 1-2*s[i]
        s[i] ^= 1
        tot += edge(i-1)+edge(i)
        res.append((tot+c1*(n-c1))//2)

    out.append(" ".join(map(str,res)))

print("\n".join(out))