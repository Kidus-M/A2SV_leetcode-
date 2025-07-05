from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    score=0
    c=Counter(a)
    for count in c.values():
        score += count //2
    print(score)