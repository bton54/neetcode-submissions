class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we can use a set to check if there's a value that appears more than once
        # go through the values
            # if they don't exist in set, add it
            # if they already do, return True
            # if we make it to the end (w/o seeing another, return False)

        # TC: O(n) - iterate through n items once
        # SC: O(n) - space used by the set if we store n items

        # alternative - we can sort and then compare neighbors
            # TC: O(n log n) - efficient sorting algortihm dominates TC, then iterate once = n
            # SC: O(1) - constant space
        
        seen = set() 

        for num in nums:
            if num in seen:
                return True
            else: 
                seen.add(num)
        return False
