import bisect

n,m=map(int,input().split())
cities=list(map(int,input().split()))
towers=list(map(int,input().split()))


r=0


for city in cities:
    pos=bisect.bisect_left(towers,city)
    d=float("inf")
    if pos<m:
        d=min(d,abs(towers[pos]-city))
    if pos>0:
        d=min(d,abs(towers[pos-1]-city))

    r=max(r,d)
print(r)