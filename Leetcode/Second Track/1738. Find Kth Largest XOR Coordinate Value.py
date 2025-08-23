class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prefix_xor = [[0] * (n + 1) for _ in range(m + 1)]

        heap = []
        for i in range(m):
            for j in range(n):
                prefix_xor[i + 1][j + 1] = prefix_xor[i + 1][j] ^ prefix_xor[i][j + 1] ^ prefix_xor[i][j] ^ matrix[i][j]
                heappush(heap, prefix_xor[i + 1][j + 1])
                if len(heap) > k:
                    heappop(heap)

        return heap[0]