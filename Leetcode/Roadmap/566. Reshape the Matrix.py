class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flatten = []
        new_mat = []
        for row in mat:
            for num in row:
                flatten.append(num)

        if r * c != len(flatten):
            return mat
        else:
            for row_index in range(r):
                new_mat.append(flatten[row_index * c: row_index * c + c])
            return new_mat