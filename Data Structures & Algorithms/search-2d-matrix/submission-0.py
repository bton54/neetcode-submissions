class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        # we can just binary search twice?


        while l <= r:
            m = (l + r) // 2

            midlist = matrix[m]

            if midlist[0] <= target <= midlist[-1]:
                # we know it's in this list, so search this list

                l2, r2 = 0, len(midlist) - 1

                while l2 <= r2: # we use <= b/c we search for a specific value

                    m2 = (l2 + r2) // 2
                    if midlist[m2] == target:
                        return True

                    elif midlist[m2] > target:
                        r2 = m2 - 1

                    elif midlist[m2] < target:
                        l2 = m2 + 1

                # if we can't find it inside of this list - returns false
                # sorted properties
                return False 

            elif target < midlist[0]:
                # the target is smaller than the current list's smallest
                # look on the left 
                r = m - 1

            elif target > midlist[-1]:
                l = m + 1

        return False