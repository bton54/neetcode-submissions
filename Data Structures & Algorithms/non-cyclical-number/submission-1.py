class Solution:
    def isHappy(self, n: int) -> bool:

        visit = set()

        while n not in visit: # while we don't have a cycle
            visit.add(n)
            n = self.sum_of_squares(n)
            if n == 1:
                return True

        # if we see it again it breaks the loop (cycle)
        return False
        
    def sum_of_squares(self, n: int):
        output = 0

        while n: # while we still have digits
            digit = n % 10
            res = digit ** 2 # square it
            output += res # add it to digit
            # process n
            n = n // 10

        return output # return it

    # TC: O(log n), SC: O(log n)
                