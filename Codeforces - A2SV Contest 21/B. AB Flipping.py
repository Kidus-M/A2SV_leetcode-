t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    count=0
    i=0
    used=[False] * (n-1)
    while i <n-1:
        if s[i]=="A" and s[i+1]=='B' and not used[i]:
            count += 1
            s[i], s[i+1] = s[i+1], s[i]
            used[i]=True
            if i >0:
                i -= 1
            else:
                i += 1

        else:
            i += 1
    print(count)