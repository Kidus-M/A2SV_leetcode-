t=int(input())


tri=[]
k=1
while True:
    x=k*(k+1)//2
    if x >t:
        break
    tri.append(x)
    k += 1


i, j=0, len(tri)-1
ok=False

while i <=j:
    s=tri[i]+tri[j]
    if s==t:
        ok=True
        break
    elif s<t:
        i += 1
    else:
        j-=1

print("YES" if ok else "NO")
