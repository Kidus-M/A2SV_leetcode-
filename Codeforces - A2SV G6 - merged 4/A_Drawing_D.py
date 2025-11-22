n=int(input())
c=n//2

for i in range(n):
    d=c-abs(i-c)
    left=c-d
    right=c+d
    print("*"*left + "D"*(right-left+1)+"*"*(n-right-1))