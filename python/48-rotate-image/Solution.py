class Solution(object):
    def rotate(self, matrix):
        new_mat=[]
        for i in range(len(matrix)):
            row=[]
            for j in range(len(matrix[0]),0,-1):
                row.append(matrix[j-1][i])
            new_mat.append(row)
        matrix[:]=new_mat
        return matrix
        # return new_mat