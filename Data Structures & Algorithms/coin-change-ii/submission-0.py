class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # instead of checking every single coin combination
        # tabulatively build up to every single possible amount, where at each step we see if it's possible to use that coin
            # if we can, we can add the number of ways we used to get to the amount - the coin (residual)

        # we can technically include this base case inside of the dp array initialization
        if amount == 0:
            return 1 # there's only one combination to get to 0 and it's nothing

        # dp[i] represents the distinct number of ways to build up to amount == i using the various coins


        dp = [0] * (amount + 1) # we want to account for the empty case

        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                # if we can make the amount using this coin, add the number of ways we can get to the previous coins
                if i - coin >= 0:
                    dp[i] += dp[i-coin]
                else:
                    break # save time since the larger coins won't even help

        return dp[amount] # answer is stored in this slot

        # TC: O(n*m) where n is the amount and m is the number of coins given to us
        # SC: O(n) where n is the amount, length of the solution array
    
        '''
        Example test case:

        amount = 4, coins = [1,2,4] /c you can use: 1 1 1 1, 1 1 2, 2 2, 1 3


        dp = [1 0 0 0 0]
        1; try coin 1. 1-1 >= 0 is true, so we can add the number of ways to reach 0. 0 + 1 = 1
        2; try coin 1, 2-1 >= 0 is true, so we can add the number of ways to reach 1. 0 + 1 = 1
            try coin 2, 2-2 >= 0 is true, so we can add the number of ways to reach 0. 1 + 1 = 2
            try coin 3 -- too large. stop checking
        3. try coin 1, 3-1 >= 0 is true, 0 + 1 = 1
            try coin 2, 3-2 >= 0 is true, 1 + 2 = 3
            try coin 3, 3-3 >= 0 is true, 3 + 1 = 4

        4. try coin 1, 4-1 >= 0 is true, 0 + 1 = 1
            try coin 2, 4-2 >= 0 is true, 1 + 2 = 3
            try coin 3, 4-3 >= 0 is true, 3 + 4 = 7.

        this is wrong. 
        '''
