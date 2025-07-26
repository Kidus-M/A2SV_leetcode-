t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    seen=False
    valid=True

    ld='0'
    ll="a"
    for c in s:
        if c.isdigit():
            if seen:
                valid=False
                break
            if c <ld:
                valid=False
                break
            ld=c
        else:
            seen=True
            if c<ll:
                valid=False
                break
            ll=c
    print("YES" if valid else "NO")