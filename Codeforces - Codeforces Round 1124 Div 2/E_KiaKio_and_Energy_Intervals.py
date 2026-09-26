import sys
from bisect import bisect_left
input=sys.stdin.readline

def solve(n,a):
    P=[0]*(n+1)
    for i in range(n):
        P[i+1]=P[i]^a[i]

    L=[0]*n
    R=[0]*n
    st=[]
    for i in range(n):
        while st and a[st[-1]]<a[i]:
            st.pop()
        L[i]=st[-1]+1 if st else 0
        st.append(i)
    st=[]
    for i in range(n-1,-1,-1):
        while st and a[st[-1]]<=a[i]:
            st.pop()
        R[i]=st[-1]-1 if st else n-1
        st.append(i)

    def check(T):
        pos={}
        for i in range(n+1):
            k=P[i]&T
            if k in pos:
                pos[k].append(i)
            else:
                pos[k]=[i]
        for p in range(n):
            if a[p]&T!=T:
                continue
            lo,hi=L[p],R[p]+1
            if p-lo<=hi-p-1:
                for i in range(lo,p+1):
                    lst=pos.get((P[i]&T)^T)
                    if lst:
                        s=max(p+1,i+2)
                        k=bisect_left(lst,s)
                        if k<len(lst) and lst[k]<=hi:
                            return True
            else:
                for j in range(p+1,hi+1):
                    lst=pos.get((P[j]&T)^T)
                    if lst:
                        e=min(p,j-2)
                        k=bisect_left(lst,lo)
                        if k<len(lst) and lst[k]<=e:
                            return True
        return False

    T=0
    for b in range(17,-1,-1):
        if check(T|1<<b):
            T |= 1<<b
    return T

t=int(input())
out=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    out.append(solve(n,a))

print("\n".join(map(str,out)))