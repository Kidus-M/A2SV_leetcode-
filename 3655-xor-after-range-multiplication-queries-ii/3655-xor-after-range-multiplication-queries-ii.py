MOD = 10**9 + 7
def mod_inverse(v):
    return pow(v,-1,MOD)
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n=len(nums)
        mop=defaultdict(list)
        for l,r,k,v in queries:
            if v==1: continue
            off = l%k
            mop[(off,k)].append((l//k,v))
            r2 = (r-off)//k + 1
            if r2*k + off<n: mop[(off,k)].append((r2, mod_inverse(v)))
        for off,k in mop:
            muls = [1]*(n//k+1)
            for i,v in mop[off,k]: muls[i]*=v
            cur=1
            for i,v in enumerate(muls):
                cur=cur*v%MOD
                ii = i*k + off
                if ii>=n: break
                nums[ii]=nums[ii]*cur%MOD
        res=0
        for v in nums: res^=v
        return res
        