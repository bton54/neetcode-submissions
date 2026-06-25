class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        n = len(nums)

        nums.sort()

        def dfs(i, path):
            # base case
            if i >= n:
                res.append(path.copy())
                return

            # first, try to take it 
            path.append(nums[i])

            dfs(i+1, path)

            # backtrack
            path.pop()

            # we now want to skip nums[i] and duplicates
            # while we have duplicates and haven't reached the end 
            while i + 1 < n and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1, path)
            
        dfs(0, [])
        return res

        # TC: O(n * 2^n) - n elements and two recursive choices. take or leave.
        # SC: O(n) - recursion stack 