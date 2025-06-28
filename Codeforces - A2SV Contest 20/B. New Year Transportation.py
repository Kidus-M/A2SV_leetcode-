n,l=map(int,input().split())
a=list(map(int,input().split()))

current=1
while current<l and current<n:
    current +=a[current-1]

if current==l:
    print("YES")
else:
    print("NO")