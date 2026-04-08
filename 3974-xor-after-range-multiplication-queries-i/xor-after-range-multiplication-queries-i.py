import numpy as np
from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1_000_000_007
        mults = np.ones(len(nums), dtype=np.int64)
        for l, r, k, v in queries:
            mults[l:r+1:k] = mults[l:r+1:k] * v % MOD
        arr = np.array(nums, dtype=np.int64) * mults % MOD
        return int(np.bitwise_xor.reduce(arr))