t=int(input())
for _ in range(t):
    n=int(input())
    x=input().strip()

    a=[]
    b=[]
    split=False

    for ch in x:
        d=int(ch)
        if not split:
            if d==0:
                a.append("0")
                b.append("0")
            elif d==1:
                a.append("1")
                b.append("0")
                split = True
            else:
                a.append("1")
                b.append("1")
        else:
            a.append("0")
            b.append(ch)
    print("".join(a))
    print("".join(b))