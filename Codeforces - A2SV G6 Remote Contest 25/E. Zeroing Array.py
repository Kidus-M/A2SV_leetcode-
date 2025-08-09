n=int(input())
a=list(map(int, input().split()))


total=sum(a)
l=max(a)

if total %2 ==0 and l<= total-l:
    print("YES")
else:
    print("NO")