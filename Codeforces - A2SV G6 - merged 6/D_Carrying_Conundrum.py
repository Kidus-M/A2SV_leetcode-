t=int(input())
for _ in range(t):
    n=input()
    a=int(n[::2])
    b=int(n[1::2]) if len(n)>1 else 0
    print((a+1)*(b+1)-2)