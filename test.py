from collections import deque
import math
import sys

input=sys.stdin.readline


t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))


    playlist=list(range(n))
    removed=[]

    pos=0
    prevgenre=None

    while playlist:
        curridx=playlist[pos]
        currgenre=a[curridx]


        if prevgenre is not None and math.gcd(prevgenre,currgenre)==1:
            removed.append(curridx+1)
            playlist.pop(pos)

            if not playlist:
                break
            if pos>=len(playlist):
                pos=0
            prevgenre=None
        else:
            prevgenre=currgenre
            pos=pos+1%len(playlist)
            if pos==0 and prevgenre==a[playlist[-1]]:
                if math.gcd(a[playlist[-1]], a[playlist[0]])==1:
                    continue
                else:
                    break
    print(len(removed), *removed)


