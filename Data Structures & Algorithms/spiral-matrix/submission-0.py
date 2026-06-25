class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # we can traverse this in a spiral order -
        # R, D, L, U and move layer by layer
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # top right
            for i in range(left, right):
                res.append(matrix[top][i])

            top += 1

            # right column, hence right - 1
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])

            right -= 1

            # stop if violating
            if not (left < right and top < bottom):
                break

            # go all the way to the left
            for i in range(right-1, left -1, -1):
                res.append(matrix[bottom-1][i])

            bottom -= 1
            for i in range(bottom -1, top - 1, -1 ):
                res.append(matrix[i][left])

            left += 1

        return res

        # TC: O(m*n)
        # SC: O(1) extra space, O(m*n) for output list
            
        

        