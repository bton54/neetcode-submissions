class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1: # returns 1; True in binary if n is ODD
                count += 1 # increment cout
            n >>= 1 # remove the last bit 
        return count

        # TC: O(1)
        # SC: O(1)

