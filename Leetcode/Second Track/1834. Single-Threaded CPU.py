class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        n = len(tasks)
        tasks = [(t[0], t[1], i) for i, t in enumerate(tasks)]
        tasks.sort()
        heap = []
        result = []
        i = 0
        current_time = tasks[0][0]

        while len(result) < n:
            while i < n and tasks[i][0] <= current_time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if heap:
                proc_time, idx = heapq.heappop(heap)
                result.append(idx)
                current_time += proc_time
            else:
                current_time = tasks[i][0]

        return result