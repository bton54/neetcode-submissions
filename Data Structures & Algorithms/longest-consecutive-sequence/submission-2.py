class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # strategy
            # place all the nums inside of the num set for quick checks on existance of values
            # go through nums
                # for each - check if this is the start of a new seqeunce
                    # if num-1 doesn't exist
                
                # if it is
                    # check how much of a sequence we can form (keep checking +1)


        if not nums:
            return 0


        num_set = set(nums)
        max_seq = 1

        for num in num_set:
            # new sequence
            if num-1 not in num_set:  

                seq = 1
                index = num

                # while we can keep finding the next value
                while (index+1) in num_set:
                    # increase sequence length
                    seq += 1
                    # compare against the max sequence
                    max_seq = max(seq, max_seq)

                    # lets check for the next index value
                    index += 1



        return max_seq

        # TC: O(n)
        # SC: O(n)

