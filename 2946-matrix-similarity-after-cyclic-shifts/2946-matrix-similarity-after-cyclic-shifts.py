class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        import copy
        shifted = copy.deepcopy(mat)
        r=len(mat)
       
        for i in range(r):
            n=len(shifted[i])
            step = k%n
            if i%2==0:
                shifted[i]=shifted[i][step:]+shifted[i][:step]
            else:
                shifted[i]=shifted[i][-step:]+shifted[i][:-step]
        return mat==shifted