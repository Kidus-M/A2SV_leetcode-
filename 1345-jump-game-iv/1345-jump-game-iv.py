from collections import deque, defaultdict
class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0
        
        val_indices = defaultdict(list)
        for i, v in enumerate(arr):
            val_indices[v].append(i)
        
        queue = deque([0])
        visited = set([0])
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                
                if i == n - 1:
                    return steps
                
                next_indices = val_indices[arr[i]] + [i-1, i+1]
                for j in next_indices:
                    if 0 <= j < n and j not in visited:
                        visited.add(j)
                        queue.append(j)
                val_indices[arr[i]][:] = []
            steps += 1
        
        return -1  