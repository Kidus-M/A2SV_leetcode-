import math
t=int(input())
for _ in range(t):
    n=int(input())
    p=[-1]*n
    i=n-1
    while i >=0:
        s=int(math.sqrt(i))
        if s*s!=i:
            s+=1
        sq=s*s
        while sq-i>=n:
            s+=1
            sq=s*s
        start=sq-i
        end=sq
        for x in range(start,end+1):
            p[i-(x-start)]=x

        i=start-1
    print(*p)