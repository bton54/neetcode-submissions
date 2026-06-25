class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # instead of a set, we can use the XOR operator

        # xor returns 
            # 0 if you put a number with itself - ex. 1 ^ 1 = 0
            # the number itself if it meets 0 - ex. 1 ^ 0 = 1

        # therefore, all numbers appearing twice cancel
        # the sole number returns 

        res = 0
        for num in nums:
            res = num ^ res #
        
        return res

        # TC: O(N) and SC: O(1)
        # Ex. 3 2 3
        # Ex Chain all of them together
        '''
            0 ^ 3 ^ 3 ^ 2
            Cancel all pairs -> 2
        '''
