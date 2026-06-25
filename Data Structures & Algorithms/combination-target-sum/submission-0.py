class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # at each step we can take the existing number or go next
        # check if we hit the sum or it went over (2 base cases)


        res = []

        def dfs(i, path_sum, path):
            if path_sum == target: # matches - copy and return
                res.append(path.copy())
                return
            if path_sum > target or i == len(nums): # target over or ran out of i
                return

            # take the same current number
            path.append(nums[i])
            path_sum += nums[i]
            dfs(i, path_sum, path)

            # skip and take the next 
            # we gotta pop and remove
            path.pop()
            path_sum -= nums[i]

            dfs(i+1, path_sum, path)

        dfs(0, 0, [])
        return res

