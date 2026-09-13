class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        l = len(img1)   
        p1, p2 = [], []                
        for r in range(l):
            for c in range(l):
                if img1[r][c] == 1:
                    p1.append((r,c))
                if img2[r][c] == 1:
                    p2.append((r,c))
        
        d = {None: 0}         
        for r1, c1 in p1:
            for r2, c2 in p2:
                v = (r1-r2, c1-c2)     
                if v not in d:
                    d[v] = 1
                else:
                    d[v] += 1
        return max(d.values())