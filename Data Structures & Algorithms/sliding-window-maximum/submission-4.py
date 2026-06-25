class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we can use a monotonic queue for this to persistently maintain the
        # largest item in the window of size k

        # we can iterate through 
            # when we have a valid window, the first element in the queue is always the largest
            # add that to th result

        # a monotonically decreasing queue ensures all following elements are less than the start
        # in this case - if we see a new greater element, we can get rid of it.



        # we store indicies in the MQ
        monotonic_queue = deque([])

        res = []

        
        for i in range(len(nums)):
            # maintain our monotonic queue:
            # while there's elements on it and the element at nums is greater than the front of the queue

            while monotonic_queue and nums[i] > nums[monotonic_queue[-1]]:
                monotonic_queue.pop() 

                # this just gets rid of every element on the queue

            # we should also remove elements that make the window invalid
                # (old elements)

            while monotonic_queue and i - monotonic_queue[0] >= k:
                monotonic_queue.popleft()


            # then, we want to push this element onto the queue
            monotonic_queue.append(i)

            # now, if we have a valid window, let's take the max element (first in the queue)
            if i >= (k-1):
                res.append(nums[monotonic_queue[0]])

        return res


        # TC: O(n)
        # SC: O(n)

'''
Input: nums = [1,2,1,0,4,2,6], k = 3

MQ = [1, 2 ]
res = []




'''
