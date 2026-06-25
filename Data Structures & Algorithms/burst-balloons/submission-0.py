class Solution:
    def maxCoins(self, nums: List[int]) -> int:
            # add the borders
        nums = [1] + nums + [1]

        # create a memoization cache
        memo = {}

        # we can solve this problem by recursively - it would be expensive so we can cache those recalculations

        def dp(l, r):
            # base case - there's no balloons between l and r
            if r - l < 2:
                return 0

            # cache time saving
            if (l, r) in memo:
                return memo[(l,r)]

            # try each balloon k in the interval range, as the last one to pop
            result = 0
            for k in range(l+1, r):
                # coin loot from popping k = l * k * r
                coins = nums[l] * nums[k] * nums[r]
                result = max(result, dp(l,k) + dp(k, r) + coins)

            memo[(l, r)] = result
            return result
        
        return dp(0, len(nums) - 1)

        # TC O(n^3), SC O(n^2)