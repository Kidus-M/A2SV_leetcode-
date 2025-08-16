from collections import Counter
t=int(input())


for _ in range(t):
    n=int(input())
    s=input().strip()

    ech=Counter(s[i] for i in range(0,n,2))
    och = Counter(s[i] for i in range(1, n, 2))


    evenC=ech.most_common(2)+[(None,0)]
    oddC=och.most_common(2)+[(None,0)]

    best=float('inf')

    for ec,ev in evenC[:2]:
        for oc,ov in oddC[:2]:
            if ec !=oc:
                changes=(n//2-ev)+(n//2-ov)
                best=min(best,changes)

    if best >0:
        bestd=best-1
    else:
        bestd=best

    print(min(best,bestd))