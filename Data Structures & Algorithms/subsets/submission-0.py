class Solution:
    def subsets(self, nums):
        res = []
        if not nums:
            return []

        n = len(nums)

        def dfs(i, path):
            # base case: if we reached the end of the list. we should stop and add it
            if i >= n:
                res.append(path.copy())
                return

            # normally, we want to add this value to the current path.
            # we can hold a list as the path for the subset.

            path.append(nums[i])
            # now we want to recurse

            dfs(i+1, path)

            # now we want to backtrack and explore the other binary option (excluding)
            path.pop()
            dfs(i+1, path)

        dfs(0, [])
        return res

        # TC: O(n * 2^n) because we have n elements and we can branch exponentially with 2 choices per step
        # SC: O(n) = depth of the recursion tree