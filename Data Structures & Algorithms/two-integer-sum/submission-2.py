class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # worst way - iterate with nested for loops to check for combos
        # space optimal
            # sort and use two pointers - (two sum 2 solution)
                # if l + r values > target ; move right ptr inwards (to lower)
                # if < target ; move left ptr to inc
                # if == target ; 
        # most time optimal
            # use a hashmap to quickly [o(1)] look up complements
            # iterate through list
                # calculate complement for each value (target - curr)
                # if it exists in the map (instant lookup), return both indices
                # otherwise, add it to the map (value -> index) 

            # use enumerate to pull index alongside num value 
            # ex. for idx, num in enumerate(nums) 


        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap: # this is key because doing "in hashmap" searches the KEYS. 
                # this is why we store the actual values as the map keys and the index in list as the map value
                return [hashmap[complement], i]
                    # we want to return the smaller index first 
                    # the cached values would always have earlier indices
                
            else:
                hashmap[num] = i

        # we are guaranteed 1 valid answer exists

        # TC: O(n) - we iterate through once and map operations are O(1) 
        # SC: O(n) - values stored in the map
        

            