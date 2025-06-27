n=int(input())
p=list(map(int,input().split()))
c=list(map(int,input().split()))

steps=1
tp=[0]*n
for i in range(1,n):
    tp[i]=p[i-1]

for i in range(1,n):
    parent=tp[i]-1
    if c[i] != c[parent]:
        steps+= 1



print(steps)




