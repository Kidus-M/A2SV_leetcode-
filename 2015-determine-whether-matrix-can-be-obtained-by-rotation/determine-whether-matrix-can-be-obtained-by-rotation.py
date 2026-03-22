class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if target == mat:
            return True
        for i in range(3):
            for j in range(len(mat)):
                for k in range(j+1, len(mat)):
                    mat[j][k], mat[k][j] = mat[k][j], mat[j][k]
                mat[j] = mat[j][::-1]
            if target == mat:
                return True
        return False