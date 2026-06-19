class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        psa=[0]*(len(gain)+1)
        psa[0]=0
        max=0
        for i in range(1,len(gain)+1):
            psa[i]=psa[i-1]+gain[i-1]
            if psa[i]>max:
                max=psa[i]
        return max