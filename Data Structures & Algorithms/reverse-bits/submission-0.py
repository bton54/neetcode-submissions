class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 
        for i in range(32): # 32 possible bits
            bit = (n >> i) & 1
            # take the right bit, and check if its odd - if so bit = 1 (True), else bit = 0 (False)
            res += (bit << 31 - i) # put this in the proper location in order ; 31-i
        return res