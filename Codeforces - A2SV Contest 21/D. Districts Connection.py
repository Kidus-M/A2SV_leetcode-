t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    diff=-1
    for i in range(1,n):
        if a[i] !=a[0]:
            diff =i
            break

    if diff==-1:
        print("NO")
        continue
    print("YES")

    for i in range(1,n):
        if a[i] != a[0]:
            print(1,i+1)
    for i in range(1,n):
        if a[i]==a[0] and i != 0:
            print(diff+1, i +1)
