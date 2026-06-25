class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            # track the number of ones per binary value
            one = 0
            # iterate through the binary representation (up to 32 bits)
            for i in range(32):
                # if we still have values in num to process AND the first element in i is 1
                # << checks the left hand side, the loop automatically pushes i
                # if n is odd, add 1
                if num & (1 << i): # if 
                    one += 1

            res.append(one)
        return res

        # TC: O(n log n)
        # SC: O(1) extra, O(n) output array

        