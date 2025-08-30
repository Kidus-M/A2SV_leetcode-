import sys
input=sys.stdin.readline
t=int(input())

for _ in range(t):
    s=input().strip()
    n=len(s)
    count=s.count("N")
    if count==1:
        print("NO")
    else:
        print("YES")


