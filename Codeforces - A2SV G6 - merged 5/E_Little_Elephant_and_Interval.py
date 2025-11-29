l,r=map(int,input().split())

def counting(n):
    if n<10:
        return n
    ans=n//10 +9

    s=str(n)


    first=int(s[0])
    last=int(s[-1])

    if last <first:
        ans-=1

    return ans


print(counting(r)-counting(l-1))