class Solution:
    def myPow(self, x: float, n: int) -> float:
        # recursively compute res = helper(x * x , n // 2)
            # we should add another multiplication if there's a remainder from n % 2
            # otherwise, just return res
        def helper(x, n):
            if x == 0:
                return 0

            if n == 0: 
                return 1

            res = helper(x * x, n // 2)
            return x * res if n % 2 else res # we return x * res or just res if it's not odd

        res = helper(x, abs(n))
        # if res is negative, the solution is 1 / res b/c exponent math
        return res if n >= 0 else 1 / res 

        # TC: O(log n), O(logn) space

            
