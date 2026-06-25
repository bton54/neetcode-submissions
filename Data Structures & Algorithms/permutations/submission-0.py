class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []


        # trick to solve permutations
            # if you flip the remaining numbers in the list depending on the start, you get the remaining permutations


        # ex. if you start with 1, then you can flip 2 and 3 to get 3 and 2
        # 2 - flip 1 and 3 to get 3 and 1

        def dfs(start):
            if start == len(nums):
                # if we have enough numbers for a permutation, copy it 
                res.append(nums.copy())

                return

            # now, we have to iterate through all the possible perms
            # the start value is fixed
            for i in range(start, len(nums)):
                # flip
                nums[start], nums[i] = nums[i], nums[start]
                # explore deeper
                dfs(start + 1)
                # flip back
                nums[start], nums[i] = nums[i], nums[start]

        dfs(0)
        return res

        # TC: O(n * n!) b/c each value has n! permuations and we have n values
        # SC: O(n) recursion depth