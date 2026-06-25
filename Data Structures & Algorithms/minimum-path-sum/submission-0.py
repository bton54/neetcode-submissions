class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # edge case - dimensions 0x0
        if not grid:
            return 0

        # get dimensionts to build the dp array to hold our solution
        rows, cols = len(grid), len(grid[0])

        # dp[row][col] = the minimum path sum from the top left to position (row,col) in the grid
        dp = [[float('inf') for col in range(cols)] for row in range(rows)]

        # base case - value of top left
        dp[0][0] = grid[0][0]

        # base case - fill in the top row
        for col in range(1, cols):
            dp[0][col] = dp[0][col-1] + grid[0][col]

        # base case - fill in the left column
        for row in range(1, rows):
            dp[row][0] = dp[row-1][0] + grid[row][0]

        # iterate through and construct our DP grid
        for row in range(1, rows):
            for col in range(1, cols):
                dp[row][col] = min(dp[row][col-1] , dp[row-1][col]) + grid[row][col]

        return dp[rows-1][cols-1]

        # TC: O(m*n), m = # of rows, n = # of cols
        # SC: O(m*n), m = # of rows, n = # of cols
        
                

        
        



