class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # we can iterate through and see if there is a 0 in each row / col

        rows, cols = len(matrix), len(matrix[0])

        row_0, col_0 = [False] * rows, [False] * cols

        # iterate through the matrix and find which rows and cols have 0s
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    row_0[r] = True
                    col_0[c] = True

        # now we want to go through the matrix and replace any values where its 0
        for r in range(rows):
            for c in range(cols):
                if row_0[r] or col_0[c]:
                    matrix[r][c] = 0


        
