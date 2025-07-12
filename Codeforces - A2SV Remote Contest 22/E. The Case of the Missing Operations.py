import heapq
n=int(input())
res=[]
heap=[]


for _ in range(n):
    s=input().strip()
    if s[0]=="i":
        x=int(s.split()[1])
        heapq.heappush(heap,x)
        res.append(s)
    elif s[0]=="g":
        x = int(s.split()[1])
        while heap and heap[0]<x:
            heapq.heappop(heap)
            res.append("removeMin")
        if not heap or heap[0]>x:
            heapq.heappush(heap,x)
            res.append(f"insert {x}")
        res.append(s)
    else:
        if not heap:
            heapq.heappush(heap,0)
            res.append("insert 0")
        heapq.heappop(heap)
        res.append("removeMin")
print(len(res))
print("\n".join(res))