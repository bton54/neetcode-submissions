class Solution:
    def findMin(self, nums: List[int]) -> int:

        ''' 
        # well, the trivial way is to simply just use the min function (iterate through) -> O(n)
        # im assuming we don't want to do this so we should use a faster -> o(log n)
        # okay, we should see what happens when we split a sample rotated list

        [3 4 5 0 1 2]

        if we binary search here, we would land on index 3 (6+0) // 2 = 3 -> 0 

        # okay, so something that i know for rotated array style search questions is to compare this to a reference point and see what info we can get
            # if we compare the index of the midpoint to the right part of the search -> r = index 5 = 2, we can tell if we're in the bigger or smaller half of the array
            # in this case, we know that since nums[mid] < nums[r], the minimum cannot after r (b/c we know mid < r and it's sorted)
                # therefore, we should include mid and search the left

            # we keep doing this until l == r -> we want to search for the minimum possible value - hence why we use while l < r and the r = mid to include mid

        # counter example:

        3 4 5 6 0 1 2

        if we binary search here we would land on index 3 again (7+0) // 2 = 3 (ignore remainder 1)
        6 > 2. this means that the minimum could probably be in the right
            we know the list is sorted, and because we're greater on the left, it definitely decreases before ascending again. so the min MUST be in that valley


        '''

        l , r = 0 , len(nums)-1


        while l < r:
            m = (l+r) // 2

            if nums[m] <= nums[r]: 
                # know that the minimum cannot be after r since it increases towards that point
                # keep mid, search the left
                # also use <= since the min of this subarray that we''re examining is AT index m

                r = m

            else:
                l = m + 1

        return nums[l] # the answer is stored at the pointer l when it converges like in search insert position
        