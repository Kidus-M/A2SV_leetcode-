class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        indices = defaultdict(list) 
        idxs = []  
        for i, num in enumerate(nums):
            idxs.append(len(indices[num]))
            indices[num].append(i)

        result = []
        for q in queries:
            qind = indices[nums[q]]
            if len(qind) == 1:
                result.append(-1)
            else:
                j = idxs[q] 
                prev = qind[(j - 1) % len(qind)]
                nextt = qind[(j + 1) % len(qind)]
                result.append(min(
                    (nextt + n - qind[j]) % n,
                    (qind[j] - prev + n) % n,
                ))

        return result