class Solution:
    def getBiggestThree(self, g: List[List[int]]) -> List[int]:
        m,n,d1,d2,res = len(g),len(g[0]),{},{},{*chain(*g)}
        for i,j in product(range(m),range(n)):
            d1[i,j],d2[i,j] = d1.get((i-1,j-1),0)+g[i][j],d2.get((i-1,j+1),0)+g[i][j]
            res.update(d1[i,j]-d1[i-k,j-k] + d1[i-k,j+k]-d1[i-k*2,j] +
                d2[i,j]-d2[i-k,j+k] + d2[i-k,j-k]-d2[i-k*2,j] - g[i][j]+g[i-k*2][j]
                    for k in range(1,min(i//2,j,n-j-1)+1))

        return nlargest(3,res)