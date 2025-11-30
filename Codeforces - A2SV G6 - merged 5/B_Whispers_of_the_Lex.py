n,d=map(int,input().split())


need= n-1
cost=0

take=min(d, need)
cost += take
need -= take

city=2

while need >0:
    cost += city
    city += 1
    need -= 1
print(cost)

