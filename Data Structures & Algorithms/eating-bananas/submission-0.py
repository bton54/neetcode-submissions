import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we're binary searching on the speeds the monkey has to eat
        # the fastest speed would be the max speed of 1 pile

        # the slowest speed is what we're trying to find - start at 1


        # we can define a helper function to see if we can actually sucessfully eat the bananas

        # if yes, we can slow it down (move the right ptr in the bs)
        # if no, we can speed it up (move the left)
        # since we're looking for an exact value, we can use l < r
            # the r = mid (instead of mid-1) and l = mid+1 


        l, r = 1, max(piles) # this is an o(n) operation though but one time only
        global_speed = r

        def can_eat(speed, piles, h):
            # given h hours, check if this speed can consume the piles

            time = 0
            # for each pile, calculate the time to eat
            for i in piles:
                hours = math.ceil(i / speed)

                time += hours

            return time <= h

        while l < r:
            mid = (l + r) // 2
            if can_eat(mid, piles, h):
                # if it's possible, try to eat slower
                r = mid
            else:
                l = mid + 1

        # since we use < it converges onto 1 value and at l - similar to the bisect / insert at left
        return l 