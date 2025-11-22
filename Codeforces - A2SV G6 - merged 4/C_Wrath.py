n=int(input())
l=list(map(int,input().split()))

kill=n+1
alive=0

for i in range(n-1,-1,-1):
    if kill<=i:
        pass
    else:
        alive+=1
    kill=min(kill,i-l[i])
print(alive)
