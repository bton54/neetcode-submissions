class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # we are trying to reach the top index _ 1 
        # we can either start at the 0 index or index 1 floor. 
        dp = [0] * (len(cost) + 1) # add 1 to account for starting on the ground

        # for the first two slots 0 and 1, we can take either the minimum cost of those two
        dp[0] = 0
        dp[1] = 0 

        # it's free to start at either

        # now we want to go through the rest of the steps and find the cheapest way to get there
        for i in range(2, len(cost)+1):
            # the cost of reaching step i is equal to the existing cost + the cost of that tile
            # take the min of this for 1 and 2 steps
            dp[i] = min((dp[i-1] + cost[i-1]), (dp[i-2] + cost[i-2]) )

        return dp[len(cost)]