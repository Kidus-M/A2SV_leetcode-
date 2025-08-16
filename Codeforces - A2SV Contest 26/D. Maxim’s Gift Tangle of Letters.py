from collections import Counter
t=int(input())


for _ in range(t):
    n=int(input())
    s=input().strip()

    if n%2==0:
        codd=[0]*26
        ceven=[0]*26
        for i, ch in enumerate(s, 1):
            c=ord(ch)-97
            if i%2:
                codd[c]+=1
            else:
                ceven[c]+=1
        half=n//2
        print((half-max(codd))+(half-max(ceven)))
    else:
        todd=[0]*26
        teven=[0]*26
        for i, ch in enumerate(s, 1):
            c = ord(ch) - 97
            if i % 2:
                todd[c] += 1
            else:
                teven[c] += 1
        podd=[0]*26
        peven=[0]*26

        sufodd=todd[:]
        sufeven=teven[:]

        l=n-1
        best=l

        for i, ch in enumerate(s, 1):
            c = ord(ch) - 97
            if i % 2:
                sufodd[c] -= 1
            else:
                sufeven[c] -= 1

            modd=0
            meven=0
            for a in range(26):
                v1=podd[a]+sufeven[a]
                modd=max(v1,modd)
                v2=peven[a]+sufodd[a]
                meven=max(meven,v2)
            best=min(best,l-(modd+meven))
            if i %2:
                podd[c]+=1
            else:
                peven[c]+=1
        print(best+1)
