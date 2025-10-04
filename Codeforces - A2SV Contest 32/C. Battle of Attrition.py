import sys
import heapq
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    p = list(map(int, input().split()))

    m=sorted(zip(h,p))
    heap=[p for _,p in m]
    heapq.heapify(heap)
    total=0
    alive=n

    i=0
    while alive>0 and k >0:
        total += k
        while i<n and m[i][0]<= total:
            heap.remove(m[i][1])
            heapq.heapify(heap)
            i+=1
            alive -=1
        if alive==0:
            break
        k-=heap[0]

    print("YES" if alive ==0 else "NO")

