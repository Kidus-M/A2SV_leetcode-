t=int(input())

for _ in range(t):
    n=int(input())
    notes=list(map(int, input().split()))

    perfect=True
    for i in range(1,n):
        diff=abs(notes[i]-notes[i-1])
        if diff not in (5,7):
            perfect=False
            break
    print("YES" if perfect else "NO")