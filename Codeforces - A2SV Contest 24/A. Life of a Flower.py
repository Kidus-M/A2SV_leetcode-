t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))



    h=1
    dead=False
    for i in range(n):
        if a[i]==1:
            if i>0 and a[i-1]==1:
                h+=5
            else:
                h+=1
        else:
            if i >0 and a[i-1]==0:
                print(-1)
                dead=True
                break

    if not dead:
        print(h)
