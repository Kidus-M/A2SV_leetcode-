t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    count=0
    ones=sum(a[:k])
    i=0

    while i <= n-k:
        if ones==0:
            count += 1
            i+=k+1
            if i <= n-k:
                ones=sum(a[i:i+k])
        else:
            if i +k<n:
                ones-=a[i]
                ones += a[i+k]
            i += 1

    print(count)