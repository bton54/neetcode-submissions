class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # edge - we have to have at least t's number of chars in s
        # we are trying to match t inside of s
        if len(s) < len(t):
            return 0

        m,n = len(s), len(t)
        
        dp = [[0 for j in range(n+1)] for i in range(m+1)]

        # we set up the dp array to 0. add 1 for the case of empty strings

        # for all values of j being 0, we set to 1
        # we gotta start at 1
        for i in range(m+1):
            dp[i][0] = 1

        # now we want to iterate through the 2D array properly and fill in the recurrence

        # at each step, if the letters match, then we have to option to:
            # take the current value of s
            # skip it

        # if they do NOT match
            # we have to skip the value in s

        # also want to start at 1 and compare backwards.
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]: # if the values in the strings are equal

                    # then we have to count the number of subsequences from matching + skipping
                        
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[m][n]



