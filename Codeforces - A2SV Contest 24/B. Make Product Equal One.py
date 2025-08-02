n=int(input())
a=list(map(int,input().split()))


cost=0
nc=0
z=0

for x in a:
    if x >1:
        cost+= x-1
    elif x<-1:
        cost+= -1 -x
        nc+=1
    elif x==-1:
        nc += 1
    elif x==0:
        z += 1
        cost += 1
    else:
        pass

if nc %2==1 and z == 0:
    cost += 2
print(cost)