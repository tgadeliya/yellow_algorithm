class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # reverse
        for i in range(len(matrix)//2):
            matrix[i], matrix[-1 - i] = matrix[-1 - i], matrix[i]  
        
        # transpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  