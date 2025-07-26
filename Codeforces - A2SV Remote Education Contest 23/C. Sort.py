t=int(input())
for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))


    cost=[]
    for i in range(n):
        cost.append(a[i]+(i+1))
    cost.sort()

    used=0
    for x in cost:
        if x<=c:
            used += 1
            c-=x
        else:
            break

    print(used)