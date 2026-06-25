class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        dp = {} # access using tuple (r,c)


        def dfs(r,c, prevVal): # coordinates + prevVal to ensure inc order
            if (r < 0 or r == rows or c < 0 or c == cols
            or matrix[r][c] <= prevVal):
                return 0

            if (r,c) in dp:
                return dp[(r,c)]

            res = 1

            res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c-1, matrix[r][c]))

            dp[(r,c)] = res

            return res

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,-1) # starting point of negative one

        return max(dp.values())

    # TC: O(m * n) due to the cache making looksup O(1) 
    # SC: O(m * n) where m is num rows and n is num cols in givne matrix
