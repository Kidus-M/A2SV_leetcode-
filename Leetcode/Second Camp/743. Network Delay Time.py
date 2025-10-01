class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for x, y, w in times:
            adj[x].append((w, y))

        processed = set()
        heap = [(0, k)]
        while heap:
            travel_time, node = heapq.heappop(heap)
            processed.add(node)

            if len(processed) == n:
                return travel_time

            for t, anode in adj[node]:
                if anode not in processed:
                    heapq.heappush(heap, (travel_time + t, anode))

        return -1